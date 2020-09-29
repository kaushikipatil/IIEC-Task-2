#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

OS_Name=form.getvalue("x")
OS_image=form.getvalue("y")

print(OS_Name)
cmd="sudo docker run -dit --name {0} {1}".format(OS_Name,OS_image)

output=sp.getstatusoutput(cmd)


status=output[0]
status1=output[1]

if status==0:
    print("Your Docker OS is launced {} ".format(OS_Name))
else:
    print("Some Error Occured Please Try Again {}".format(status1))