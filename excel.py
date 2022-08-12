from cmath import isnan
from math import nan
import pandas as pd

table=pd.ExcelFile('TOTAIS MP BAT SAP copy.xlsx').parse("vencidas")
#print(table)
#lendo o número de uma nota d emp
#note='000'+str(table.loc[0, 'NOTA'])
#print(note)
#escrevendo o número de uma nova nota dp
#table.loc[1, 'NOTA DP']=256
#print(table)
#reescrevendo planilha
df=pd.DataFrame(table)
#df.to_excel('PREVENTIVAS.xlsx')
size=len(df['NOTA DP'])
i=1
#fazendo teste se a celula esta preenchida 

while i < size:
    if df.loc[i, 'NOTA DP'] == nan:
        note='000'+str(df.loc[i, 'NOTA'])
        print('nota de mp:', note, type(note))
    else:
        print('nota dp já existe: ', df.loc[i, 'NOTA DP'], type(df.loc[i, 'NOTA DP']))
    i=i+1

    

