
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 80                # Reserve a port for your service.

print( 'Connecting to ', host, port)
s.connect((host, port))

while True:
  msg = b"Hello"
  print( 'sending to server >> ', msg)
  s.send(msg)
  msg = s.recv(1024)
  print( 'revieved from server >> ', msg)
#s.clos