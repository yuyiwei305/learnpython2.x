#! /usr/bin/env python


L=["1","2","3","8","4","1"]

def fanxiang(x,y):
	if x < y:
		return 1
	if x > y:
		return -1
	return 0

print sorted(L,fanxiang)


def zhushi():
	print "---------------------"
zhushi()
def cmp_str(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0


M=["Chenzhuo", "Zhujing","alice","black" ,"davail"]

print sorted(M,cmp_str)
