# Nama : sinta Alfi Royanul M
# ML-27

# Import library yang diperlukan
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Memuat dataset
hour_data = pd.read_csv("https://raw.githubusercontent.com/sintaalfirm/bikesharingdataset/refs/heads/main/hour.csv")
day_data = pd.read_csv("https://raw.githubusercontent.com/sintaalfirm/bikesharingdataset/refs/heads/main/day.csv")

# Set judul dashboard
st.title("Dashboard Sewa Sepeda")

# Pertanyaan 1: Bagaimana variasi sewa sepeda berdasarkan musim?
st.header("Distribusi Sewa Sepeda Berdasarkan Musim")
season_fig, season_ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=hour_data, ax=season_ax)
season_ax.set_title('Distribusi Sewa Sepeda Berdasarkan Musim')
season_ax.set_xlabel('Musim')
season_ax.set_ylabel('Total Sewa Sepeda')
season_ax.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
st.pyplot(season_fig)

# Insight dari Pertanyaan 1
st.write("Analisis: Anda dapat melihat bagaimana sewa sepeda bervariasi berdasarkan musim. Musim panas cenderung memiliki sewa yang lebih tinggi dibandingkan dengan musim lainnya.")

# Pertanyaan 2: Apa tren sewa sepeda berdasarkan hari dalam seminggu?
st.header("Total Sewa Sepeda Berdasarkan Hari dalam Seminggu")
day_data['day_of_week'] = day_data['weekday'].map({0: 'Min', 1: 'Sen', 2: 'Sel', 3: 'Rab', 4: 'Kam', 5: 'Jum', 6: 'Sab'})
day_fig, day_ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='day_of_week', y='cnt', data=day_data, ax=day_ax, order=['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'])
day_ax.set_title('Total Sewa Sepeda Berdasarkan Hari dalam Seminggu')
day_ax.set_xlabel('Hari dalam Seminggu')
day_ax.set_ylabel('Total Sewa Sepeda')
st.pyplot(day_fig)

# Insight dari Pertanyaan 2
st.write("Analisis: Dari diagram batang, Anda dapat melihat hari mana yang memiliki sewa sepeda tertinggi. Hari kerja seperti Senin dan Jumat mungkin menunjukkan pola sewa yang berbeda dibandingkan dengan akhir pekan.")
