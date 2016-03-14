#! /usr/bin/env python

classmate= [ "wanglelei","chenzhuo","saolei","zhujing","liubo"]

#print classmate

friend = ( "zhanglei" , "zhuyongchao", classmate)

#print friend

for name in friend:
	x = type(name)
	if str(x) == "<type 'list'>" :
		for name2 in name:
			print name2
	else:
		print name

