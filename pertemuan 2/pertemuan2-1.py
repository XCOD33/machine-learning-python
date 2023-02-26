# libraries
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
import pandas as pd
import numpy as np

# baca file dataset
df = pd.read_csv("Apartemen_ok.csv")

# melihat semua isi data
print(df)
le = LabelEncoder()

for col in df.columns.values:
    # encoding pada variabel kategorial
    if df[col].dtypes == 'object':
        unique_values = df[col].unique()
        le.fit(unique_values)
        df[col] = le.transform(df[col])
        data = pd.concat([df[[col]], df[[col]]])
df.head(10)
print(df)

# simpan data
df.to_csv("Apartemen_numerik.csv", header = True, index = False)