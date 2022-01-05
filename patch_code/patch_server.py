import os                             
import pickle
import hashlib
import hmac
def reverse_fun():
 with open("users.json","rb") as f:
  data = f.read()
  r_signature,read_data=data.split(b' ')
  new_signature=hmac.new(b'secret',read_data,hashlib.sha256).digest()    # for example only writing the secret here only , developer can import from other file as his choice
  if new_signature==r_signature:
   return(pickle.loads(read_data))
  else:
   return("Check Failed , cannot read")         
if __name__ == '__main__':
  print(reverse_fun())

