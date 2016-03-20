#! /usr/bin/env python


import os

a = os.path.abspath('.')
b= os.path.join(a,"testdir")
print b
os.mkdir(b)
with open(b+"/"+"test.txt","w+") as f:
	f.write("I Love U \n ChenZhuo")

