#-*-coding:utf-8-*-

from collections import defaultdict
members=[
    #Sex,name
    ['male','John'],
    ['male','Jack'],
    ['female','Lily'],
    ['male','Pony'],
    ['female','Lucy'],
]

result=defaultdict(list)
for sex ,name in members:
    result[sex].append(name)
print result
    
    
    
