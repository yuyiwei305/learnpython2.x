#! /usr/bin/env python


def date():
	print "2016-03-18"


def zhushi():
	print "-------------------"

f = date

f()

print f.__name__


zhushi()

def log(func):
	def tishi(*agr,**sth):
		
		print " call %s() " % func.__name__

		return func(*agr,**sth)
	return tishi




@log
def date2():
	print "2016-03-18-16.53"

date2()




@log
def zhushi2():
	print "=----------------="

zhushi2()
