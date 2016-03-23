#! /usr/bin/env python


from xml.parsers.expat import ParserCreate
import re

class DefaultSaxHandler(object):
	def start_element(self,name,attrs):
		print "sax : start_element : %s ,attrs : %s " % (name , attrs)


	def end_element(self,name):
		print "sax : end_element : %s " % name
		
	def char_data(self,text):
		print "sax : char_data : %s" % text
	        if  re.match(r'Python' , text):
			print text+"!!!!!!!"
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python" log = "23333333333333">Python</a></li>
    <li><a href="/ruby" log = "wo ai chen zhuo ">Ruby</a></li>
</ol>
'''



handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler  = handler.char_data
parser.Parse(xml)
