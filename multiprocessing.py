#! /usr/bin/env python

import os

print "process (%s) start..." %  os.getpid()

pid = os.fork()

if pid ==0 :
	print "i an child process \n"
else:
	print "i am  dad process (%s), my son is (%s)\n" % (os.getpid(),pid)


