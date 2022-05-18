'''
data transaksi dari tahun 2013 sampai dengan 2019
Field yang ada pada data tersebut antara lain:

1. No
2. Row_Num
3. Customer_ID
4. Product
5. First_Transaction
6. Last_Transaction
7. Average_Transaction_Amount
8. Count_Transaction

'''

#Import dan Inspeksi data
import pandas as pd
df = pd.read_csv('dataretail.csv', sep=';')

#print(df.head())
#print(df.info())

'''
--- Hasil inspeksi ----
1. Kolom 'no' dan 'Row_Num' tidak diperlukan untuk modeling -> hapus
2. Kolom 'First_Transaction' 'Last_Transaction' belum berbentuk datetime -> ubah jadi datetime
---YJP---
'''


#Hapus kolom yang tidak diperlukan ---YJP---
del df['no']
del df['Row_Num']
#Ubah format ke datetime ---YJP---
df['First_Transaction']= pd.to_datetime(df['First_Transaction']/1000, unit='s', origin='1970-01-01')
df['Last_Transaction']= pd.to_datetime(df['Last_Transaction']/1000, unit='s', origin='1970-01-01')


'''
---kategorisasi is_churn true atau fase--- 
Note: Dinyatakan churn jika customer tidak bertransaksi lagi setelah 6 bulan dari transaksi terakhir seluruh data.
---YJP--- 
'''


transakasi_terakhir = max(df['Last_Transaction'])
# print(transakasi_terakhir) -> hasil 2019-02-01 23:57:57.286000128
df.loc[df['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True 
df.loc[df['Last_Transaction'] > '2018-08-01', 'is_churn'] = False

#Data is_churn masih bertipe object ubah ke boolean
df['is_churn'] = df.is_churn.astype(bool)



'''
---Pembuatan tambahan kolom--- 
Untuk data visualisasi dan model prediction diperlukan data:
1. Tahun Pertama Transaksi (Year_First_Transaction) 
2. Tahun Terakhir Transaksi (Year_Last_Transaction)
3. Perbedaan tahun transaksi pertama dan terakhir (Year_Diff) 
---YJP--- 
'''
df['Year_First_Transaction'] = df['First_Transaction'].dt.year
df['Year_Last_Transaction'] = df['Last_Transaction'].dt.year
df['Year_Diff'] = df['Year_Last_Transaction'] - df['Year_First_Transaction']

''' 
------data yang telah siap diolah------
''' 
