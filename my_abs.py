#! /usr/bin/env python

def my_abs(x):

	if x>=0:
		return x
	else:
		return -x


a = raw_input("pls echo a int code : ") 
a = int(a)
print my_abs(a)
