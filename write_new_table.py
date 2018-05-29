import sys
import pandas as pd

varFil = sys.argv[1]
df = pd.read_csv(varFil, header=0, sep='\t')
print len(df)

df_new = df[df['Allele Call'].isin(['Heterozygous', 'Homozygous'])]

print len(df_new)

df_res = df_new[df_new['Allele Cov'] >= 30]

print len(df_res)

df_res.to_csv('output.xls', index=False, header=True, sep='\t')

writer = pd.ExcelWriter('outputExcel' + '.xlsx')
df_res.to_excel(writer, 'Sheet1', index=False)
writer.save()