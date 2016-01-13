# short script to search .bash_history
# based of command cat .bash_history | grep ___, where ___ is whatever is being searched for
# http://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/
 
# http://www.pythonforbeginners.com/os/subprocess-for-system-administrators

import subprocess
from subprocess import Popen,PIPE


keyword = raw_input("Enter the text you want to search for\n")

#a = subprocess.Popen("who", stdout = subprocess.PIPE, shell = True)
#(output, err) = a.communicate()

#p1 = Popen(["write", usn[parsed_users_index].strip(), spot[parsed_users_index]], stdin=PIPE, stdout=PIPE)

#p1 = Popen(["cat", ".bash_history", "|","grep",keyword], stdin=PIPE, stdout=PIPE)

#subprocess.call(["cat", ".bash_history", "|","grep","*"])
#subprocess.call(["ls", "-l"])

command = "cat "+ ".bash_history "+"| "+"grep "+ keyword
p = subprocess.Popen('grep %s .bash_history' % keyword, stdout=subprocess.PIPE, shell=True)
#print subprocess.check_output('grep python *.txt', shell=True)

#subprocess.Popen(command, shell=True)