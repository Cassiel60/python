#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import pandas as pd
#传入表格并读取
varfil=sys.argv[1]
df1=pd.read_excel(varfil,header=0,seq='\t')
#print len(df1)
varfil=sys.argv[2]
df2=pd.read_excel(varfil,header=0,seq='\t')
#print len(df2)
#判断相同位点的疾病是否相同
for line1 in df1['dbSNP']:
  if df2['dbSNP'] is line1:
     df2['Diseases_CN'].replace('df2['Diseases_CN']','df1['Diseases_CN']')
  else:
  	continue

      