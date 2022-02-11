import pandas as pd
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import json
import numpy as np 

kaggle = {"username":"layllaalencar","key":"dbd499a65b108aef8347444951a46782"}
with open('kaggle.json', 'w') as file:
    json.dump(kaggle, file)

#BUSCANDO DADOS DA API
api = KaggleApi()
api.authenticate()

api.dataset_download_file('ealaxi/banksim1',
                              file_name= 'bs140513_032310.csv')
#EXTRAINDO OS DADOS


dados_brutos = pd.read_csv('bs140513_032310.csv.zip', index_col= False, delimiter = ',')
dados_brutos.head()
df = dados_brutos

#Criando coluna ID:
df['id'] = df.index + 1
df = df.reindex(columns=['id'] + list(df.columns[:-1]))
print(df)

#Transformando coluna Age em int:
print(df.dtypes)
print(df['age'].unique())
df["age"] = df["age"].map(lambda x: x.replace("'",""))
df["age"] = df["age"].replace(["U"], '0')
df = df.astype({'age': 'int'})
print(df['age'].unique())
print(df)

#Deixando coluna gender com M e F:

print(df['gender'].unique())
df["gender"] = df["gender"].map(lambda x: x.replace("'",""))
df["gender"] = df["gender"].replace(["U", "E"], "0")
print(df['gender'].unique())

#Deixando null Amount onde a coluna for 0:
print(df['amount'].unique())
df["amount"] = df["amount"].replace(0, np.nan)
print(df['amount'].unique())


#Criando coluna ano:
df['year'] = df.index + 1
df['year'] = df['year'] = 2022
print(df)


#Criando coluna mês:
df['month'] = df.index + 1
df.loc[(df["step"] <= 30), "month"] = "01"
df.loc[(df["step"] > 30) & (df["step"] <= 60), "month"] = "02"
df.loc[(df["step"] > 60) & (df["step"] <= 90), "month"] = "03"
df.loc[(df["step"] > 90) & (df["step"] <= 120), "month"] = "04"
df.loc[(df["step"] > 120) & (df["step"] <= 150), "month"] = "05"
df.loc[(df["step"] > 150) & (df["step"] <= 180), "month"] = "06"
print(df['month'].unique())
print(df)


#Criando coluna data: 
df['day'] = df.index + 1
df['day'] = df['day'] = 1
print(df)

df.columns = df.columns.str.lower()

