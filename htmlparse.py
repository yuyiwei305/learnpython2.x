#! /usr/bin/env python

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import re

class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if len(attrs) == 0 :
			pass
		else:
			for (variable , value) in attrs:
				if variable == "href" and re.match(r'^http://',value):
					print value
	def handle_endtag(self,tag):
		pass
#		print "</%s>" % tag
	def handle_startendtag(self,tag,attrs):
		pass
#		print "</%s>" % tag
	def handle_data(self,data):
		pass
#		print "%s" % data
	def handle_commit(self,data):
		pass
#		print "<!----->"
	def handle_entityref(self,name):
		pass
#		print "%s" % name
	def handle_charref(self,name):
		pass
#		print "$#@%s" % name

parser = MyHTMLParser()
f = open("./htmlparser.html" , "r")
d = f.read()
parser.feed(d)	
f.close()
print "--------------------"
