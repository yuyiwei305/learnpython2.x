#! /usr/bin/env python

def guifan(x):
	return x[0].upper() + x[1:].lower()

l=["woaini","chenzhuo","zhujing", "aLISs"]


print map(guifan,l)

def zhushi():

	print "----------------"


zhushi()

def prod(L):
	m=[]
	for i in range(len(L)):
		a=int(L[i])
		m.append(a)
	return m
def cheng(x,y):	
	return x*y
h=["1","3","5","7"]
u=[1,2,3,4]
print reduce(cheng,prod(u))
