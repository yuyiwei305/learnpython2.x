#! /usr/bin/env python

try:
	import cPilckle as pickle
except ImportError:
	import pickle

d= dict(name='chenzhuo',age=20,score=89)
f = open("dump.txt","w+")
pickle.dump(d,f)
f.close

f = open('dump.txt',"r+")
d=pickle.load(f)
f.close()
print d
