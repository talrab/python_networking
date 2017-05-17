import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receive(name,sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                data = data.decode()
                print("Received from: " + str(addr) + ": " + str(data))
        except:
            pass
        finally:
            tLock.release()


client_host = '127.0.0.1'
client_port = 0  # 0 means it will find a free port available on the computer

server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((client_host,client_port))
s.setblocking(0)  #set non blocking

rT = threading.Thread(target=receive,args=("RecvThread", s))
rT.start()

alias = input("Name:")
message = input(alias + '-> ')
while message != 'q':
    if message != '':
        s.sendto("{}: {}".format(alias, message).encode(), server)
    tLock.acquire()
    message = input(alias + '-> ')
    tLock.release()
    time.sleep(0.2)

shutdown = True
rT.join()
s.close()



