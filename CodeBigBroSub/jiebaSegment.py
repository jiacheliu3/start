#coding=gbk
'''
Created on 2015��9��24��

@author: Tassadar
'''

import sys

import jieba.analyse.textrank
import jieba.analyse.extract_tags

#a=sys.argvs[1]
s=u'���ʲô��һ��'
f=open("F:\\testOutput.txt","a")
print(jieba.analyse.extract_tags(s,3))
print(jieba.analyse.extract_tags(s,3),file=f)
f.close()