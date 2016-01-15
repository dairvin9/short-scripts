# Made by Denise Irvin
# January 7th, 2016
# Short python script to decrypt a file that was encrypted by encrypter.py.



fileName = input("Which file would you like to decrypt?\n")
print ("Decrypting " + fileName)

file = open(fileName, 'r+')

fileContents = file.read()
fileContentsList = fileContents.split('\n')

#decryption logic

#Change this
shiftNumber = fileContentsList[0]

#Change this
#Converts the file to binary representation, which is 7 bits long
fileContents = ''.join(format(ord(x)+int(formatNumber), 'b') for x in fileContents)

file.write(''.join(format(ord(x), 'b') for x in formatNumber))
file.write(fileContents)
 
file.close()        
