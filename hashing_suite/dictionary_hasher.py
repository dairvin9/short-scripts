# July 31, 2016
# simple program that hashes a list of passwords into an output file

import hashlib

dictionary_file_name = input('What is the name of your dictionary?: ')

#loads Dictionary/wordlist
list = open(dictionary_file_name,'r')
lst = list.read()
list.close()
dictionary = lst.split()

output_file = open('hashes.txt','w')

x=0
# Look for matches
while (x<len(dictionary)):
	to_be_hashed = dictionary[x].encode('utf-8') 
	m = hashlib.md5(to_be_hashed).hexdigest()
	
	# Writes the string and its hash to a file
	output_file.write(dictionary[x] + ' ' + m + '\n')
	x += 1
	
output_file.close()