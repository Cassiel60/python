'''
table AD contains RS,ADID;table Parkinson contains RS,PDID;table variant contains ADID,
PDID insert table variant 
one way: below
two way: by merge
'''
import sys ,re
import pandas as pd

varfil1=r'C:\Users\BAIOMED07\Desktop\AD_Database_20170629.xls' 
varfil2=r'C:\Users\BAIOMED07\Desktop\parkinson_TOTAL.xls'
varfil3=r'C:\Users\BAIOMED07\Desktop\alleles_IonXpress_066.txt'

df1=pd.read_excel(varfil1)
print df1.head(1)
df2=pd.read_excel(varfil2)
print df2.head(1)
df=df1[df1['dbSNP'].isin(df2['dbSNP'])]

print df.head(2)

df.to_excel('1.xlsx',index=0)

df3=pd.read_csv(varfil3,sep='\t')
df3['pkiq']='-'
for index,row in df2.iterrows():
	
	rs=row['dbSNP']
	row1=df1[df1['dbSNP']==rs]
	if not len(row1): continue      # when drug locus is not in row1
	#import pdb; pdb.set_trace()
	uniq=row1['UniqueID'].values.tolist()[0]

	row2=df3[df3['Allele Name']==uniq]
	df3.loc[row2.index,'pkiq']=row['UniqueID']
print df3.head(1)
res_1=df3[df3['Allele Name'].isin(df['UniqueID'])]
res_1.to_excel('2.xlsx',index=0)

