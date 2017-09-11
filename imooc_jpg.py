# -*- coding:utf-8 -*-
#地址需要改成自己设定的地址
import re,os
import urllib2
urls='http://www.imooc.com/course/list?page='
s=int(raw_input("how many pages:"))
if s>32 or s<1 :
    print "your input is error"
else :
    for i in range(s):
        os.mkdir('E:\\ceshi\\'+str(i+1))
        req=urllib2.urlopen(urls+str(i+1))
        buf=req.read()
        listurl1=re.findall(r'http:.+?\.jpg',buf)
        list_all=[listurl1[x] for x in range(len(listurl1)) if x%2==1]
        count=1
        for url in list_all:
            imgpath='E:\\ceshi\\'+str(i+1)+'\\'
            with open(imgpath+str(count)+'.jpg','wb') as f:
                re_url= urllib2.urlopen(url)
                buf_url = re_url.read()
                f.write(buf_url)
            count+=1
        print 'page %s is finash!' % (i+1)

