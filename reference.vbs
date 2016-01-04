'Reference
'This will have basic stuff, because it is mostly a syntax cheat sheet

'Oddly enough, keywords don't seem to be case sensitive

'How to do loops
Dim index  
index = 5 
Wscript.echo VarType(index) 'shows the number 2, which indicates that index is an integer

Do While index < 8  'the loop itself. Until can be used instead of While

index = 1 + index
Wscript.echo "Jeremiah was a bullfrog"

Loop 'end of loop


