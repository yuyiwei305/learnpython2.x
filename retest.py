#! /usr/bin/env python

import re
name = "chenzhuo"
test = "chenzhuo.qq.gmail@qq.com"

if re.match(r'.*@\w*\.com$', test):
	print " %s \'s mail is %s" % (name,test)

else :
	print "%s \'s mail is bad!..." % name

print "----------------------------------------"


''' re.split'''


a = "wo ai    ni"

print a.split(' ')

print re.split(r'\s+',a)

print "----------------------------------------"



#reemail = re.compile(r'([0-9a-zA-Z.]+)@([0-9a-zA-Z_.]+)') 

remail = re.compile(r'(\w*)(.+)@(\w*\.com)$')
if remail.match(test) :	
	print test
