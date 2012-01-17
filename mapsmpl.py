# -*- coding: utf-8 -*-

def printNum(x):
	print "put out %d" % x

List = [2,3,4,5,6]

map(printNum,List)
print map(lambda x: x +1,List)
print reduce(lambda x,y: x+y,List)
print filter(lambda x: x > 3,List)
