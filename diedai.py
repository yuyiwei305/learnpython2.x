#! /usr/bin/env python

from collections import Iterable
def zhushi():

	print "--------------------"



zhushi()
d = { 'a':1,'b':2,'c':3,'d':"wo ai ni chen zhuo" }
print d
zhushi()

for i in d:
	print i
zhushi()

for i in d:
	print d[i]
zhushi()

print isinstance('abc' ,Iterable) 

print isinstance([1,2,3,4],Iterable)

print isinstance((1,2,3,4,5,6,7),Iterable)

zhushi()

zuobiao=[(1,1),(2,3),(5,7),(4,9)]

print zuobiao 
zhushi()
for x in zuobiao:
	print x
zhushi()

for x,y in zuobiao:
	print x,y

zhushi()

