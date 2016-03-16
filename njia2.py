#! /usr/bin/env python

L=[]
n=1
while n<=99:
	L.append(n)
	n=n+2
print L
r=[]
m=3
for i in range(m):
	r.append(L[i])

print r

print L[0:3]
