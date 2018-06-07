#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 

import requests
import pdb
from bs4 import BeautifulSoup
output=file('out.xls','w')
for i in range(1,27):

	res=requests.get('http://www.caae.org.cn/gzneurosci/scn1adatabase/scn1a_variant.php?page=%d'% i)
	res.encoding='utf-8'
	soup=BeautifulSoup(res.text,'lxml')
	tr1=soup.select('.tr1')
	tr0=soup.select('.tr0')
	header=tr1[0].select('th')
	n=len(header)
	head='\t'.join([header[i].text for i in range(n)])
	output.write(head+'\n')
	n1=len(tr1)
	n0=len(tr0)
	for num in range(n1):
		if num>0:
			con=[]
			con1=tr1[num].select('td')
			col=len(con1)
			con='\t'.join([con1[col_num].text for col_num in range(col)])
			output.write(con+'\n')

	for num in range(n0):
		if num>0:
			con=[]
			con1=tr0[num].select('td')
			col=len(con1)
			con='\t'.join([con1[col_num].text for col_num in range(col)])
			output.write(con+'\n')

output.close()
