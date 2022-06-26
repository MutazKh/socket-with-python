import socket 
s = socket.socket()
print ('server created...')
host = socket.gethostname()
#you should have the same port of the client
port = 9999
s.bind(('localhost',port))
s.listen(5)
print ('wait please...')
while True:
  c, addr = s.accept()
  x = c.recv(1024).decode()
  if x == 'quit':
    print ('')
    
  print ('get connection from ',addr, x)
  c.close()    
