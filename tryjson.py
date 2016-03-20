#! /usr/bin/env python

import json

d = dict(name="chenzhuo",socre=90,age=20)
print json.dumps(d)

def zhushi():
	print "--------------------"
zhushi()

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age  = age
		self.score= score

def turnstudenttojson(obj):
	return {
	'name' : obj.name,
	'age'  : obj.age,
	'score': obj.score
	}


s = Student("chenzhuo",20,86)
print json.dumps(s,default=lambda s : s.__dict__)




