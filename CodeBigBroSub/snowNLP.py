#coding=gbk
'''
Created on 2015年9月25日

@author: Tassadar
'''

# Requirement:unicode
from snownlp import SnowNLP
import sys

input=sys.argv[1]
output=sys.argv[2]

print(input)

content=open(input,"r").read()

#the number of keywords is set about square root of length
from math import *
length=ceil(sqrt(len(content)))



r=SnowNLP(content)
#print(r.keywords(10, False))
outSnowNLP="C:\\Users\\Tassadar\\Desktop\\Course\\weibo\\temp\\snowOutput.txt"
outSnowF=open(outSnowNLP,"w")
f=open(output,"w")


result=r.keywords(length, False)
print("\n",file=f)
print("\n",file=outSnowF)
for x in result:
    print(x,end="\n",file=f)
    print(x,end="\n",file=outSnowF) 
print(r.keywords(length, False))


f.close()