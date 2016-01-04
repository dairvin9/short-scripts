'simple vbscript to create files

'object.CreateTextFile(filename[, overwrite[, unicode]]) if unicode = false, then it is ascii. if overwrite is false, if a file has the same name it will not be overwritten
'https://msdn.microsoft.com/en-us/library/5t9b5c0c(v=vs.84).aspx reference


Dim fileSystemObject, quoteFile
Set fileSystemObject = CreateObject("Scripting.FileSystemObject")
Set quoteFile = fileSystemObject.CreateTextFile("quoteFile.txt", True)
quoteFile.WriteLine("It's a trap.")
quoteFile.Close
