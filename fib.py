#! /usr/bin/env python

L=[x*x for x in range(11)]
print L
G=(y*y for y in range(11))
print G
for n in G:
	print n
print "---------------------------"
def fib(max):
	n,a,b,temp=0,0,1,0
	while n<max:
		print b
		temp=b
		b=b+a
		a=temp
		n=n+1
fib(6)
'''c = int(raw_input("pls a max num: ")
fib(c)'''



