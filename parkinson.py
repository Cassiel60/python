#coding=utf-8
import pandas as pd 
import pdb
import re

varfil1=r'C:\Users\BAIOMED07\Desktop\parkinson_Database_20170619.xlsx' 
varfil2=r'C:\Users\BAIOMED07\Desktop\parkinson.txt'

out = open('parkinson.xls','wb')

df1=pd.read_excel(varfil1)

df2=pd.read_csv(varfil2,header=0,sep='\t')['#Phynotype'].values.tolist()
#df2=open('parkinson.txt')
sum=0

for index1,row in df1.iterrows():
	value1 = row['CLNDBN']
	
	newrow = ''  #add blank string
	need = False
	for index2,value2 in enumerate(df2):
		if str(value1).upper().__contains__(str(value2).upper()):
			need = True
			break

			# sum+=1
			# print index1,value1
			# print sum
			# res.append(row)
			# #pdb.set_trace()
			# print res
			
	if need:
		newrow = str(index1)
		for val in row.values:
			tmp = ' '
			try:
				tmp = str(val).decode('utf-8').encode('gb2312')
			except:
				pass

			newrow += '\t' +tmp
		newrow+='\n'

		out.write(newrow)

	        
out.flush()
out.close()

