# Reads information from a file and prints it out one word at a time


f = open('quoteFile.txt', 'r')

rawInput = f.read()

words = rawInput.split()

for word in words:
    print (word)
