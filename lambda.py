#! /usr/bin/env python


print map(lambda x : x*x, [1,2,3,4,5,6,7,8])

print "--------------------"

L= [(lambda x=x: x*x*x) for x in range(1,4)]

for i in range(len(L)):
	print L[i]()
