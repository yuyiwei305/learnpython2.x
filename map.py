#! /usr/bin/env python

def f(x):
	return x*x
L=[]
for i in range(10):
	L.append(i)

print L	

def zhushi():
	print "---------------------------"

zhushi()

print map(f,L)
zhushi()

print map(str,L)
zhushi()
''' reduce'''

def fn(x,y):
	return x+y

print reduce(fn,L)
