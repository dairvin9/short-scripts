# IF you have a file with passwords and their hashes, separated by whitespace, one after the other, you can use this to see if a given hash matches any of the hashes in the dictionary. If it does, this will tell you the original password. If you need a dictionary, see dictionary_hasher.py

import hashlib

to_be_cracked = input('The file with the hash to crack: ')

#grab the hash you want to crack
file = open(to_be_cracked,'r')
to_be_cracked = file.read()
file.close()


dictionary_file = input('The dictionary with the hashes: ')
previously_hashed_dictionary_file = open(dictionary_file,'r')
previously_hashed_dictionary = previously_hashed_dictionary_file.read().split()
previously_hashed_dictionary_file.close()

x=0
found = False
while (x<len(previously_hashed_dictionary)):

	
	if (to_be_cracked == previously_hashed_dictionary[x+1]):
		print ("The password is {}".format(previously_hashed_dictionary[x]))
		found = True
	x += 2
#output_file.close()
if not found:
 print ("The dictionary didn't have your password :(")