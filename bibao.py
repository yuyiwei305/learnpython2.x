#! /usr/bin/env python


def count():
	L=[]
	for i in range(1,5):
		def f():
			return i*i
		L.append(f)

	return L

a = count()
for x in range(len(a)):
	print a[x]()
def count2():
	 M=[]
	 for i in range(1,5):
		def f(j):
			def g():
				return  j*j
			return g
		M.append(f(i))
	 return M

b = count2()
for y in range(len(b)):
	print b[y]()



