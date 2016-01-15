# Made by Denise Irvin
# January 7th, 2016
# Short python script to encrypt a file, using a simple original algorithm.

import random

fileName = input("Which file would you like to encrypt?\n")
print ("Encrypting " + fileName)

file = open(fileName, 'r+')

fileContents = file.read()

formatNumber = input("Give me a number:\n")

formatNumber = str((int(formatNumber) * random.randrange(2,777))% 1000) #increase entropy

#Converts the file to binary representation, which is 7 bits long
fileContents = ''.join(format(ord(x)+int(formatNumber), 'b') for x in fileContents)

file.write(''.join(format(ord(x), 'b') for x in formatNumber))
file.write(fileContents)
 
file.close()        
