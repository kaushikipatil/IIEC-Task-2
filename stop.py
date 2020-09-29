#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

form=cgi.FieldStorage()
OS=form.getvalue("i")
#OS=input("Enter a OS name: ")

cmd1="sudo docker stop {}".format(OS)

run1=sp.getstatusoutput(cmd1)

status1=run1[0]
status2=run1[1]

if status1==0:
    print("Your Docker OS has been Stopped.. {}".format(OS))
else:
    print("Some error occur".format(status2))