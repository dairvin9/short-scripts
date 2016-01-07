# Made by Denise Irvin
# January 5th, 2016
# Short python script to write a new line to the end a file, prexisting or not


fileName = input("Which file would you like to append to?\n")
print ("Appending/creating to " + fileName)

file = open(fileName, 'a')

keepAppending = True

print("Type 'done' to stop adding lines to the file")

while keepAppending:
    line = input("Type the line you would like to add, or 'done' to finish.\n")
    if line == "done":
        keepAppending = False
    else:
        file.write(line + '\n')    
file.close()        
