#! /usr/bin/env python

def app_end(L=None):
	if L is None:
		L=[]
	L.append("end")
	print "-------------------"
	return L

a=[1,2,3]
app_end(a)
print a
b=[]
app_end(b)
print b
app_end(b)
print b
print app_end()
print app_end()

