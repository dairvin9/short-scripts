#!/usr/lib/python
import sys
import fileinput
from subprocess import call
import subprocess
import thread
import select as my_select
from time import sleep

# Function to asynchronously print system output
def print_std_out(f):
    if f:
        while True:
            out = f.stdout.read()
            if out == "" and f.poll() != None:
                break
            else:
                print out 

while True:
    sleep(.5)
    print "What do you want to do?"
    request = raw_input()
    request_parts = request.split(' ')
    proc = subprocess.Popen(request_parts, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE) # .stdout.read()
    
    try:
        thread.start_new_thread ( print_std_out, (proc,) )
    except Exception as e:
        print str(e)
    
    while True: 
        if proc.poll != None:
            break
        request = raw_input()
        request_parts = request.split(' ')
        #proc.communicate(input=request_parts')[0]
        #sleep(.5)
        #print "What do you want to do?"
        #request = raw_input()
        #request_parts = request.split(' ')
        
        
        
        
	

	
  
	
