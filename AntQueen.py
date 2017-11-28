ant = """ \  \  
 |__/ _   .-.
(o_o)(_`>(   )
 { }//||\\`-'"""
k = 1
while k > 0:
	file_name = "ant%s" % k
	try:
		file = open(file_name, 'w')
		file.write(ant)
		file.close()
	
	except:
		print "Turn off your computer before its too late!"
		print "Srsly Dennis"
	
	k = k + 1
