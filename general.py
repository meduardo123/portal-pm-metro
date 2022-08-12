from os import system
import functions as f
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

 #isso deve ser temporário. o driver é definido no arquivo functions
table=pd.ExcelFile('TOTAIS MP BAT SAP copy.xlsx').parse("vencidas")
df=pd.DataFrame(table)
username='r325493'
password='Ago32246'
i=1
while i<=2:
    note='000'+str(df.loc[i, 'NOTA'])
    dp_number=f.login(username, password, note)
    print('número da nota do desvio: ')
    print(dp_number)
    print (i)
    i=i+1
    
exit()


