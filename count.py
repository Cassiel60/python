import pandas as pd
import sys

var=sys.argv[1]
df=pd.read_excel(var)

count=df.groupby('CLINSIG').size()
T=len(df['CLINSIG'])
a=count.loc['Pathogenic']
b=count.loc['Likely pathogenic']
c=count.loc['Likely benign']
try:
	d=count.loc['Benign']
except:
	d=0
e=T-a-b-c-d
print type(count)
print a,b,c,d,e


