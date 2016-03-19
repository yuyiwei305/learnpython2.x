#! /usr/bin/env python 


class Student(object):
	def __init__(self,name):
		self.__name=name

	def print_name(self):
		return self.__name
	def __str__(self):
		return "%s is a good boy" % self.__name


a = Student("yuyiwei")

print a.print_name()
print a
print "========================"



class Chain(object):
	def __init__(self,path="/users"):
		self.path = path
	def users(self,path):
		return Chain("%s/%s" % (self.path,path))
	def __getattr__(self,path):
		return Chain("%s/%s" % (self.path,path))
	def __str__(self):
		return self.path
	__repr__=__str__

a = Chain().users('myj').etc.list
print a
b= Chain()
print b
c = Chain().mian.list
print c
d = Chain().main.chen.zhuo
print d
		
