#! /usr/bin/env python 

with open("/var/log/boot.log","r") as f:
	print f.read()
def zhushi():
	print "---------------"
zhushi()


f = open("./test.txt","w")
f.write("Wo ai ChenZhuo\n")
f.write("wo ai wanglelei\n")
f.close()
with open("./test.txt","a+") as f:
	f.write("hello\n")

f = open ("./test.txt" ,"r")
print f.read()
f.close()

