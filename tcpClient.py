import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))   #who to we want to connect to?


    message = input('->')
    while message !='q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print ("Received from server: " + data)
        message = input("->")
    s.close()

if __name__ == '__main__':
    Main()


