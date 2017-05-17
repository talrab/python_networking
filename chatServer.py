import socket
import time

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   # a UDP socket
s.bind((host,port))
s.setblocking(0)

users = []

print ("Server started on " + host + ":" + str(port))

while True:
    try:
        data,addr = s.recvfrom(1024)
        data = data.decode()
        print("Connected to: " + str(addr))
        print(time.ctime(time.time()) + " Received from " + str(addr) + ":: " + str(data))
        if addr not in users:
            users.append(addr)
        for user in users:
            print("Sending to " + str(user) + ": " + str(data))
            s.sendto(data.encode(),user)
    except:
        pass

s.close()







