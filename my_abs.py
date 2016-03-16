#! /usr/bin/env python

def my_abs(x):
	
	if not isinstance(x, ( int, float) ):

		raise TypeError("bad operand type!")

	if x>=0:
		return x
	else:
		return -x

a=10
print my_abs(a)
print " a is a intager"
b=-20
print my_abs(b)
print "b is a fu shu "
c= "a"
print my_abs(c)
print " c is a zifu"
