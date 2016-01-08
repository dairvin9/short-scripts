# Made by Denise Irvin
# January 7th, 2016
# Short python script to write a new line to the end a file, prexisting or not

fileName = input("Which file would you like to encrypt?\n")
print ("Encrypting " + fileName)

file = open(fileName, 'r+')

fileContents = file.read()

formatChoice = input("Pick a format: binary, character, decimal, octal or hex:\n")

if formatChoice == "b" or formatChoice == "binary":
    fileContents = fileContents.format()


file.write(fileContents)
 
file.close()        
