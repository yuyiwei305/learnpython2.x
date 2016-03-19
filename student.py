#! /usr/bin/env python

class Student(object):

	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score =  score
		else:
			print "bad score"




	def print_score(self):
		print "%s : %s" % (self.__name , self.__score)

	
	def get_grade(self):
		if self.__score >= 90:
			print "%s\'s grade is A " % self.__name
		elif self.__score >= 80:
			print "%s\'s grade is B" % self.__name
		elif self.__score >= 70:
			print "%s\'s grade is C" % self.__name
		else :
			print "%s\'s grade is D" %self.__name
 
	def zhushi(self):
		print "----------------------"
	def zongchengji(self):
		
		self.print_score()
		self.get_grade()
		self.zhushi()

chenzhuo = Student("chenzhuo",76)
zhujing = Student("zhujing",88)
wanglelei=Student("wanglelei",99)
zhanghuan= Student("zhanghuan",59)
'''chenzhuo.print_score()
zhujing.print_score()
wanglelei.print_score()
zhanghuan.print_score()
chenzhuo.get_grade()
zhujing.get_grade()
wanglelei.get_grade()
zhanghuan.get_grade()
'''

chenzhuo.zongchengji()
zhujing.zongchengji()
zhanghuan.zongchengji()
wanglelei.zongchengji()
chenzhuo.set_score(90)
chenzhuo.zongchengji()
