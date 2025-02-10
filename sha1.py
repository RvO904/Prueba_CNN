import hashlib

sha1sum = hashlib.sha1()
with open('temp.wav', 'rb') as source:
  block = source.read(2**16)
  while len(block) != 0:
    sha1sum.update(block)
    block = source.read(2**16)
print(sha1sum.hexdigest())