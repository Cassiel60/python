#!/usr/bin/python
#-*-coding:utf-8-*-

import re

line = 'cats are smarter than dogs'

matchobj = re.match(r'(.*) are (.*?) .*',line, re.M|re.I)

if matchobj:
    print 'matchobj.group() :',matchobj.group()
    print 'matchobj.group(1) :',matchobj.group(1)
    print 'matchobj.group(2) :',matchobj.group(2)
print (re.search('www','www.runoob.com').span())
print (re.search('com','www.runoob.com').span())

matchobj=re.match(r'dogs',line,re.M|re.I)
if matchobj:
    print 'match-->matchobj.group():',matchobj.group()
else:
    print 'no match!!'

matchobj=re.search('dogs',line,re.M|re.I)
if matchobj:
    print "search-->matchobj.group():",matchobj.group()
else:
    print "no match!!"


#------------------------------------------------------------------------
phone='2004-959-559 # 这是一个国外电话号码'

#删除字符串中的python注释
num=re.sub(r'#.*$','',phone)
print u'电话号码是：',num
#删除非数字的字符串
num=re.sub(r'\D','',phone)
print u'电话号码是：',num

#-----------------------------------------------------------------------

#将匹配的数字乘以2
def double(matched):
    value=int(matched.group('value'))
    return str(value*2)
s='A23G4HFD567'
print (re.sub('(?P<value>\d+)',double,s))
