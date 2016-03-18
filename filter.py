#! /usr/bin/env python

def is_odd(x):
	return x%2 ==1

n=range(21)
print n

print filter(is_odd,n)


def sushu(x):
	for i in range(2,x-1):
		if x%i==0:
			return False
	return True

print filter(sushu,range(100))


