# Made by Denise Irvin
# January 5th, 2016
# Short python script to write a new line to the end a file, prexisting or not


fileName = input("Which file would you like to append to?\n")
print ("Appending/creating to " + fileName)

file = open(fileName, 'a')

keepAppending = True

while keepAppending:
    line = input("Type the line you would like to add.\n")
    file.write(line + '\n')
    line = input("Hit Enter to add another line, and any other key to continue.\n")
    if line != "":
        keepAppending = False

file.close()        
