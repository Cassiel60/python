#!/usr/bin/env python3
# encoding: utf-8

import pandas as pd 
import sys
import pdb

varfil=sys.argv[1]
f=open('2.xls','w')
f.write('name'+'\t'+'ID'+'\t'+'age'+'\t'+'B'+'\t'+'L'+'\t'+'yuejing'+'\t'+'doctor'+'\t'+\
'shisan'+'\t'+'shiba'+'\t'+'eryi'+'\t'+'caiyang'+'\t'+'jieshou'+'\t'+\
'tai'+'\t'+'IVF'+'\t'+'shisanrisk'+'\t'+'shibarisk'+'\t'+'eryirisk'+'\n')
df=pd.read_csv(varfil,header=0,sep='\t')
df.to_csv('12.txt',index=False,header=True)
x=4
for i in range(x):
	m=i+1
	df_res=df.iloc[78*i:78*m]
	lst=df_res.values.tolist()
	ID=lst[3][0].split(':')[-1]
	name=lst[12][0]
	age=lst[13][0]
	B=lst[26][0].split(',')[1].split(':')[-1].strip(']')
	L=lst[26][0].split(',')[3].split(':')[-1].strip(']')
	yuejing=lst[16][0]
	doctor=lst[24][0].split(' ')[-1]
	shisan=lst[37][0]
	shiba=lst[38][0]
	eryi=lst[39][0]
	caiyang=lst[19][0].split(' ')[0]
	jieshou=lst[23][0].split(' ')[1]
	tai=lst[10][0].split(' ')[-1]
	IVF=lst[17][0].split(' ')[-1]
	shisanrisk=lst[45][0].strip('[]')
	shibarisk=lst[46][0].strip('[]')
	eryirisk=lst[47][0].strip('[]')
	f.write(name+'\t'+ID+'\t'+age+'\t'+B+'\t'+L+'\t'+yuejing+'\t'+doctor+'\t'+\
	shisan+'\t'+shiba+'\t'+eryi+'\t'+caiyang+'\t'+jieshou+'\t'+\
	tai+'\t'+IVF+'\t'+shisanrisk+'\t'+shibarisk+'\t'+eryirisk+'\n')
