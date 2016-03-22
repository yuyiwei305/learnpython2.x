#! /usr/bin/env python


import os,sys,hashlib,getpass
from collections import defaultdict
try:
	import cPickle as pickle
except ImportError:
	import pickle


class Resign(object):

	def __init__(self):
		self.__user={}
		self.__set = 0

	def __mimamd5(self,user,passwd):
		md5 = hashlib.md5()
		md5.update(user+passwd)
		return md5.hexdigest()
	def usertest(self,user):
		
                if self.__user.has_key(user):
                        return False

	def regedit(self,user,passwd):

		if self.usertest(user) is not False:
			self.__user[user] = self.__mimamd5(user,passwd)
			print "-----------------------------"
			print " %s created success! " % user
			return 0
		else :
			print "------------------------"
			print " the user has regedited"
			return -1

	def login(self,user,passwd):
		if not self.__user.has_key(user):
			print " the user have not regedit"
		else:
			if self.__user[user] == self.__mimamd5(user,passwd):

				self.__set = 1
				
			else:
				self.__set = -1
				
	def zhuangtai(self):

		if self.__set == 1 :
			print "--------------------"
			print "welcome my world!!"
		if self.__set == -1:
			print "--------------------"
			print "bad passwd!! "

	def setuser(self,d):
		self.__user = d
		return self.__user
				


	def getuser(self):
		return self.__user
def getuser():
	user = Resign()
	f = open("./db.txt" , "r")
        d = pickle.load(f)
        f.close()
        user.setuser(d)
	name = user.getuser()
	for i in name :
		print "%s" % i
	username = raw_input("pls input your username: ")
	while True:
                userpasswd1 = getpass.getpass("Enter your passwd: ")
                userpasswd2 = getpass.getpass("pls repeat you passwd: ")
                if userpasswd1 == userpasswd2 :
                        userpasswd = userpasswd1
                        break
                else :
                        print "pls renzhen yidian....  input again! \n"
                        continue
	user.regedit(username,userpasswd)
	d = user.getuser()
	return d
def userlogin():
	user = Resign()
	username = raw_input("pls input your username: ")
	userpasswd = getpass.getpass("Enter your passwd: ")
	f = open("./db.txt" , "r")
	d = pickle.load(f)
	f.close()
	user.setuser(d)
	user.login(username,userpasswd)
	user.zhuangtai()


''' ------------------------------------------------------------------------------------'''	
def usage():
        print "------------- usage ------------------"
        print " input  \"regedit\" for  regedit "
        print " input  \"login\" for login"
        print " input  \"showuser\" for show user"
        print " default : usage"
	print "------------- usage ------------------"


'''  try load db '''
try :
	f = open("./db.txt","r")
	d = pickle.load(f)
	
except IOError :
	f.close()
        f = open("./db.txt","w")
        d = {}
        pickle.dump(d,f)
except EOFError:
	f.close()
	f = open("./db.txt","w")
	d = {}
        pickle.dump(d,f)
finally:
	f.close()
''' load db down , start go main '''



try:
        liucheng = sys.argv
	gongneng = ["regedit","login","showuser"]
	print liucheng

	if liucheng[1] == "regedit" : 		
		get_user = getuser()
		f = open("./db.txt","w")
		pickle.dump(get_user,f)
		f.close()
		print "------------------------"
	
	elif liucheng[1] == "login":
		userlogin()
		print "------------------------"

	elif liucheng[1] == "showuser":
		print "------------------------"
		f = open("./db.txt","r")
		d = pickle.load(f)
		f.close()
		for i in d:
        	        print "%s : %s" % (i , d[i])			

		print "------------------------"
	else:
		usage()
except IndexError:
        usage()



