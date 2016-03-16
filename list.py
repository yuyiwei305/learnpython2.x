#! /usr/bin/env python
import os
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
def zhushi():

	print "----------------------------------"

zhushi()

range(1,11)
L=[]
for x in range(1,11):
	L.append(x*x)
x=None
print L
	
zhushi()
sancifang=[x*x*x for x in range(1,11)]
print sancifang 

zhushi()


oushusancifang=[x*x*x for x in range(1,11) if x % 2 == 0 ]
print oushusancifang

zhushi()

dir=[d for d in os.listdir('/')]
print type(dir)
print dir
for x in dir :
	print x
zhushi()
changdu=len(dir)

print changdu


for z in range(changdu):
	print dir[z]

zhushi()

foreverlove={ "mymother" : "pangyoumei","mydad":"yuli","mydog":"mengduo","andMy": "VisIon"}
print foreverlove.iteritems()
for x,y in foreverlove.iteritems():
	print x,"=",y

