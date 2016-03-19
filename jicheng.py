#! /usr/bin/env python

class Animal(object):
	def run(self):
		print " Animal is running"

class Dog(Animal):
	def run(self):
		print "dog is running"

a = Animal()
a.run()
def zhushi():
	print "--------------"
zhushi()
b = Dog()
b.run()
zhushi()

print isinstance(a,Animal)
print isinstance(b,Dog)
print isinstance(b,Animal)

def runtwice(Animal):
	Animal.run()
	Animal.run()
print dir(a)
runtwice(a)
runtwice(b)
