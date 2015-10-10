
'''
Created on 2015��10��3��

@author: Tassadar
'''



import urllib
import json
import time
import urllib.request
from urllib.parse   import quote

#global params
inputPath="C:\\Users\\Tassadar\\Desktop\\Course\\weibo\\UserWeibos201201"
outputPath="C:\\Users\\Tassadar\\Desktop\\Course\\weibo\\UserWeibos201201_en"
s=""
tempHolder=""
#check whether to run
counter=1;
outputFile=open(outputPath, "a",encoding="utf-8")

import re
uselessStart = re.compile("^[0-9]+\t?\|\|\t?\|\|\t?-?[0-9]+\t[\u4e00-\u9fa5a-zA-Z\-_0-9]+\t")
atUser=re.compile('@[\u4e00-\u9fa5a-zA-Z\-_0-9]+')
blanks=re.compile('(\\N\t)*')


#def readNextItem(input):
    
def wait():
    print("Reached threshold, wait 1h")
    time.sleep(3600)
    
def translate(string):
    #get string from file
    orgStr=string
    #pre-processing before translation
    #strip out the names and tagging
    str=uselessStart.sub("", orgStr)
    str=atUser.sub("",str)
    str=blanks.sub("",str)
    print("Translation src: "+str)
    URL = 'http://openapi.baidu.com/public/2.0/bmt/translate?from=%s&to=%s&q=%s&client_id=%s'
    API_Key = 'AQdkTPm4GH7dQz6fZaGFdmpU' #换成自己的APIKey
    url = URL % ("zh", "en", quote(str), API_Key)
    
    header={}
    header['from']="zh"
    header['to']="en"
    header['client_id']=u'AQdkTPm4GH7dQz6fZaGFdmpU'
    header['q']=quote(str);
    
    #request = urllib.request.Request(url)
    #print(request.read())
    print(url)
    response = urllib.request.urlopen(url).read().decode('utf-8')
    print (response)
    rs = json.loads(response)
    # check error
    if 'error_code' in rs:
        err_code=rs['error_code']
        print("Error detected!")
        err_msg=rs["error_msg"]
        print(err_code+": "+err_msg)
        return
    # if no error
    global outputFile
    print(orgStr,file=outputFile)
    inEng=rs['trans_result']
    for i in inEng:
        
        print(i['dst'])
        print(i['dst'],file=outputFile)
    print("End of this translation")
    #print the result to the 
    


#entrance
with open(inputPath,"r",encoding="utf-8") as input:
    for line in input:
        if counter<30:
            print(str(counter)+"th translation of the hour")
            set=[line[i:i+1999] for i in range(0, len(line), 1999)]
            for next in set:
                translate(next)
                counter+=1
            
        else:
            wait()
outputFile.close()