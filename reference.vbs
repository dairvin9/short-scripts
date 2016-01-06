'Reference
'This will have basic stuff, because it is mostly a syntax cheat sheet

'Oddly enough, keywords don't seem to be case sensitive

'Loops
Dim index  
index = 5 
Wscript.echo VarType(index) 'shows the number 2, which indicates that index is an integer

Do While index < 8  'the loop itself. Until can be used instead of While

index = 1 + index
Wscript.echo "Jeremiah was a bullfrog" 'Way better than hello world

Loop 'end of loop

'If Statements
' If the body of the statement is only one line, you dont need the End If
Dim value
value = 6
If value=5 Then
Wscript.echo("And a good friend of mine")
Wscript.echo("...")
End If
If value=6 Then
Wscript.echo("Kindness is loving people more than they deserve")
Wscript.echo("...")
End If
