# libraries
import numpy as np
import pandas as pd

# baca file dataset
# df = pd.read_csv("apartemen2.csv")

# melihat semua isi data
# print(df)

# cek ada missing value?
# print(df.isnull().values.any())

# banyaknya missing value
# print(df.isnull().sum().sum())

# melihat kolom KodeApt
# print(df['KodeApt'])
# print(df['KodeApt'].isnull())

# melihat kolom jumlah kamar
# print(df['Jum_kamar'])
# print(df['Jum_kamar'].isnull())

# membuat daftar missing value
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("apartemen2.csv", na_values = missing_values)
# print(df['Jum_kamar'])
# print(df['Jum_kamar'].isnull())
# print(df['St_Milik'])
# print(df['St_Milik'].isnull())

# Deteksi angka
cnt=0
for row in df['St_Milik']:
  try:
    df['St_Milik'].isnull()
    int(row)
    df.loc[cnt, 'St_Milik'] = np.nan
  except ValueError:
    pass
  cnt+=1
# print(df["St_Milik"].isnull())

# total missing value tiap kolom
# print(df.isnull().sum())

# banyaknya missing values
# print(df.isnull().sum().sum())

# mengganti missing values dengan sebuah angka
df["KodeApt"].fillna(837, inplace=True)
# print(df.KodeApt)

# mengganti pada lokasi spesifik
df.loc[2, "KodeApt"] = 8837
# print(df.KodeApt)

# mengganti missing value dengan median
median = df["Jum_kamar"].median()
df["Jum_kamar"].fillna(median, inplace=True)
# print(df.Jum_kamar)
# print(df)

# mengganti pada lokasi spesifik pada kolom St_Milik
df.loc[3, 'St_Milik'] = 'N'
df.loc[6, 'St_Milik'] = 'Y'
# print(df.St_Milik)

# simpan data
df.to_csv('Apartemen_ok.csv', header=True, index=False)