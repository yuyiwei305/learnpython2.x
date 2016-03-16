#! /usr/bin/env python

def power(x,n=2):
	s=1
	while(n>0):
		n=n-1
		s=s*x
	return s

a = int(raw_input("pls input a  numper: "))
b = int(raw_input("pls input other  numper: ")) or 2
	
print power(a,b)


		
		
