#! /usr/bin/env python


class Student(object):



	def get_score(self):
		return self.__score

	def set_score(self,score):
		if not isinstance(score,int):
			raise ValueError("it must a num!")
		if score < 0 or score > 100:
			raise ValueError("score must in 1~100")
		self.__score = score

a = Student()
a.set_score(20)
print a.get_score()

def zhushi():
	print "--------------------"


class Student2(object):
	@property
	def score(self):
		return self.__score

	
	@score.setter
	def score(self,score):
		if not isinstance(score,int):
			raise ValueError("score must num !!")
		if score < 0 or score > 100 :
			raise ValueError("score must in 1~100 !")
		self.__score = score

b = Student2()
b.score = 90

print b.score	
