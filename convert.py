#!/usr/bin/env python
from BeautifulSoup import BeautifulStoneSoup
import os
import sys

class Log(object):
	def __init__(self,file):
		self.log = BeautifulStoneSoup(open(file).read())
	def convert(self):
		for ele in self.log.chat.findAll(['event','message']):
			if ele.name=='event':
				ele = Event(ele)
				print ele.sender,ele.type
			elif ele.name=='message':
				ele = Message(ele)
				print ele.alias,':',ele.text

class Event(object):
	def __init__(self,ele):
		print >> sys.stderr, ele.name, ele.attrs
		self.ele = ele
		self.attrs = ele.attrs
		self.sender = ele['sender']
		self.type = ele['type']

class Message(object):
	def __init__(self,ele):
		print >> sys.stderr, ele.name, ele.attrs
		self.ele = ele
		self.attrs = ele.attrs
		self.alias = ele['alias']
		self.text = BeautifulStoneSoup(ele.find(text=True),convertEntities=BeautifulStoneSoup.XML_ENTITIES)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		file = sys.argv[1]
	else: # Get Testing Log
		file = os.listdir('testlogs')[0]
		file = os.path.join('testlogs',file)
	
	# Redirect debugging
	sys.stderr = open('/dev/null','w')
	
	log = Log(file)
	log.convert()
