#! /usr/bin/env python

def jiecheng(n):
	if n==1:
		return 1
	n=n*jiecheng(n-1)
	return n

print jiecheng(5)




