#This code receives an audio file from a client and saves it in a temporal wave file

import socket               # Import socket module
import sys
import hashlib

s = socket.socket()         # Create a socket object
host = '10.253.37.50'# Get local machine name
port = 9696                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('temp.wav','wb')
s.listen(5)                 # Now wait for client connection.
while True:
  c, addr = s.accept()     # Establish connection with client.
  print('Got connection from', addr)
  print( "Receiving...")
  l = c.recv(1024)
  while (l):
      print ("Receiving...")
      f.write(l)
      l = c.recv(1024)
  f.close()
  print ("Done Receiving")

  #Now, calculate the sha1 of the temp wav file
  sha1sum = hashlib.sha1()
  with open('temp.wav', 'rb') as source:
    block = source.read(2**16)
    while len(block) != 0:
      sha1sum.update(block)
      block = source.read(2**16)
  
  file_sha1 = sha1sum.hexdigest()
  c.send(file_sha1.encode())

  #c.send('Thank you for connecting')
  c.close()   