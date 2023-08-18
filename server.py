import socket
import pickle
import struct
import imutils
srvr_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

port = 80

srvr_sock.bind((host_ip,port))
print("socket bind complete")
srvr_sock.listen(5)
print("Now listening")
# c, addr = srvr_sock.accept()     # Establish connection with client.
while True:
  cl_sock,addr =  srvr_sock.accept() 
  print( 'Got connection from', addr)
  if cl_sock: 
    
  msg = cl_sock.recv(1024)
  print( addr, ' <<<<< ', msg)
  cl_sock.send(b"Hai")
  print( addr, ' >>>>> ', "Hai")
  