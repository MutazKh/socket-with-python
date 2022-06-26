import socket
while True:
     s = socket.socket()
     #you should put the same port in both server and client
     port = 9999
     s.connect(('localhost',port))
     #the variable X are send to the server
     x = input('server:~$ ')
     s.send(bytes(x,'utf-8'))
     print (s.recv(1024).decode())
     #here if you want to close, only write quit
     if x == 'quit':
        print ('server end')
        break

