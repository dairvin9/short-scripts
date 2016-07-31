# Cheap hasher
# A simple program you can use to get the (md5) hash of a string
import hashlib

to_be_hashed = input("Give me something to hash:")
to_be_hashed = to_be_hashed.encode('utf-8') 
m = hashlib.md5(to_be_hashed).hexdigest()
print (m)
