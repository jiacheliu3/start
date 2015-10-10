#coding:gbk
'''
Created on 2015年9月25日

@author: Tassadar
'''

# Requirement:unicode
import jieba
from jieba.analyse import textrank
from jieba.analyse import extract_tags
import sys
import ftplib


input=sys.argv[1]
output=sys.argv[2]

print(input)

content=open(input,"r").read()

from math import *
length=ceil(sqrt(len(content)))


e=extract_tags(content,length)
t=textrank(content,length)
#print(r.keywords(10, False))

#use 2 files as output for comparison
outT="C:\\Users\\Tassadar\\Desktop\\Course\\weibo\\temp\\jiebaTDIFD.txt"
outR="C:\\Users\\Tassadar\\Desktop\\Course\\weibo\\temp\\jiebaTextRank.txt"
fT=open(outT,"w")
fR=open(outR,"w")

outF=open(output,"w")

print("\n",file=fT)
for x in e:
    print(x,end="\n",file=fT)
    print(x,end="\n",file=outF) 
print("\n",file=fR)
for x in t:
    print(x,end="\n",file=fR) 
    print(x,end="\n",file=outF)

fT.close()
fR.close()
outF.close()