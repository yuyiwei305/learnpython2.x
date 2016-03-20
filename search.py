#! /usr/bin/env python

import os
import sys


def search(path,key):
	for x in os.listdir(path):
		if os.path.isfile(os.path.join(path,x)) and key in os.path.split(x)[1]:
			print os.path.join(path,x)
		if os.path.isdir(x):
			search(os.path.join(path,x),key)
		

args = sys.argv

search(os.path.abspath('.'),args[1])
