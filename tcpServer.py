import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()    #default is a TCP socket
    s.bind((host,port))

    s.listen(1) #listening for one connection at a time
    c, addr = s.accept()    # c is a new socket object usable to send and receive data on the connection, and addr is the address bound to the socket on the other end of the connection
    print ("connection from: " + str(addr))

    while True:
        data = c.recv(1024).decode()   #num of max bytes
        if not data:
            break
        print ("from connected user: " + data)
        data = data.upper()
        print("Sending: " + data )
        c.send(data.encode())
    c.close()

if __name__ == '__main__':
    Main()

