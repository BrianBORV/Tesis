import pandas as pd


#xls= pd.ExcelFile("prueba.xls")
#print(xls.sheet_names)
#a=xls.sheet_names
#df=xls.parse(a)
#print(df)

df= pd.read_excel('prueba.xls', skiprows=2, usecols="B")
a=len(df)
print(df)
print(type(df))
arreglo=df.values

print(arreglo[20])


