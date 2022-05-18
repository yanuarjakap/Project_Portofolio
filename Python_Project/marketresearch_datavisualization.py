import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from marketresearch_datapreparation import df


df_2bulan = df.loc[((df['First_Transaction'] <= '2019-02-02' ) 
                   & (df['First_Transaction'] >= '2019-01-01' )) 
                   | ((df['First_Transaction'] <= '2018-02-02' ) 
                                      & (df['First_Transaction'] >= '2018-01-01' )) 
                   | ((df['First_Transaction'] <= '2017-02-02' ) 
                                      & (df['First_Transaction'] >= '2017-01-01' ))
                   | ((df['First_Transaction'] <= '2016-02-02' ) 
                                      & (df['First_Transaction'] >= '2016-01-01' ))
                   | ((df['First_Transaction'] <= '2015-02-02' ) 
                                      & (df['First_Transaction'] >= '2015-01-01' ))
                   | ((df['First_Transaction'] <= '2014-02-02' ) 
                                      & (df['First_Transaction'] >= '2014-01-01' ))]

'''
----Customer Acquisition----
'''

# Customer Aquisiton per tahun dalam tahun
df_year = df.groupby(['Year_First_Transaction'])['Customer_ID'].count()
df_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar', title='Graph of Customer Acquisition')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()

plt.show()

# Customer Aqusition per tahun dalam dua bulan pertama - karena data tahun 2019 baru berjalan 2 bulan
df_year = df_2bulan.groupby(['Year_First_Transaction'])['Customer_ID'].count()
df_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar', title='Graph of Customer Acquisition\nJan-Feb')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()

plt.show()

"""
----Insight Customer Aquisition(CA)-----

# Grafik.Customer Aquisition(CA) per Tahun
    1. Berdasarkan Grafik.Customer Aquisition(CA) per Tahun : Data CA relatif terus meningkat, sedikit menurun di 2018 dan turun drastis di 2019
    2. Penurunan Drastis di 2019 karena di tahun tersebut baru berjalan 2 bulan. -> Perlu analisa performa CA per tahun pada 2 bulan pertama

# Grafik.Customer Aquisition(CA) per Tahun pada dua bulan pertama
    1. Terjadi peningkatan CA pada 2 bulan pertama setiap tahunnya

---Insight---
---Secara umum tim Marketing telah melakukan strategi marketing yang tepat di 2 bulan pertama tahun 2019---

"""

sns.pointplot(data = df_2bulan.groupby(['Product', 'Year_First_Transaction']).mean().reset_index(), 
              x='Year_First_Transaction', 
              y='Average_Transaction_Amount', 
              hue='Product')
plt.show()

"""
----Insight Average Transaction Amount-----


# Grafik.Average Transaction Amount (TA) per Tahun pada dua bulan pertama
    1. Baju merupakan product dengan TA terbesar ditahun 2018 dan menurun drastis di tahun 2019
    2. Jakert merupakan produk yang TA nya terus meningkat stabil per tahun
    3. Sepatu mengalami tren penurunan sejak tahun 2015
    4. Tas mengalami peningkatan drastis di tahun 2019

---Insight---
1. Perlu ada perubahan strategi marketing untuk produk baju dan sepatu.
2. Strategi marketing untuk tas dan jaket sudah tepat

"""


df_piv = df.pivot_table(index='is_churn', 
                        columns='Product',
                        values='Customer_ID', 
                        aggfunc='count', 
                        fill_value=0)
# Mendapatkan Proportion Churn by Product
plot_product = df_piv.count().sort_values(ascending=False).head(5).index
# Plot pie chartnya
df_piv = df_piv.reindex(columns=plot_product)
df_piv.plot.pie(subplots=True,
                figsize=(10, 7),
                layout=(-1, 2),
                autopct='%1.0f%%',
                title='Proportion Churn by Product')
plt.tight_layout()
plt.show()

"""
----Insight Proportion Churn by Product-----

# Grafik.Average Transaction Amount (TA) per Tahun pada dua bulan pertama
    1. 60% customer pada semua produk menjadi churn
    2. Jaket memiliki angka tertinggi dengan 68%

---Insight---
Perlu dilakukan perbaikan layanan dan kualitas produk agar customer bisa terus aktif bertransaksi

"""