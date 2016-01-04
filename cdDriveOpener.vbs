'Silly script to open cd drive
'do not have a cd drive on current computer, so it is untested

Set oWMP = CreateObject("WMPlayer.OCX.7" )  
Set colCDROMs = oWMP.cdromCollection  
 
if colCDROMs.Count >= 1 then  
For i = 0 to colCDROMs.Count - 1  
colCDROMs.Item(i).Eject  
Next ' cdrom  
End If  
 