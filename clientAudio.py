import socket               # Import socket module
import sys
import hashlib

s = socket.socket()         # Create a socket object
host = '10.253.46.5' # Get local machine name
port = 9696                 # Reserve a port for your service.

s.connect((host, port))

#Before sending, store sha1 of wav file
import hashlib
sha1sum = hashlib.sha1()
with open('temp.wav', 'rb') as source:
  block = source.read(2**16)
  while len(block) != 0:
    sha1sum.update(block)
    block = source.read(2**16)

file_sha1 = sha1sum.hexdigest()

#Send file
f = open('sample.wav','rb')
print('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
#s.shutdown(socket.SHUT_WR)

#Receive the sha1 string from the server
s.shutdown(socket.SHUT_WR)
sent_file_sha1 = s.recv(1024).decode()

if(file_sha1 == sent_file_sha1):
   print('Sent successfully')

s.close  