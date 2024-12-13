import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_hr = pd.read_csv('data-bike/hour.csv')
data_day = pd.read_csv('data-bike/day.csv')


# Fungsi untuk plot pola penggunaan sepeda berdasarkan musim
def plot_season_usage(season_data):
    season_data.columns = ['season', 'cnt_mean', 'cnt_sum', 'casual_mean', 'registered_mean']
    plt.figure(figsize=(6, 7))
    sns.barplot(x='season', y='cnt_mean', data=season_data, palette='viridis', hue='season', dodge=False)
    plt.title('Rata-rata Penyewaan Sepeda per Musim ', fontsize=14)
    plt.xlabel('Musim', fontsize=12)
    plt.ylabel('Rata-rata Penyewaan', fontsize=12)
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Winter', 'Spring', 'Summer', 'Fall'])
    plt.legend([], [], frameon=False)
    st.pyplot(plt)

# Fungsi untuk plot pola penyewaan sepeda berdasarkan jam
def plot_hourly_usage(hourly_pattern, selected_hours):
    # Jika tidak ada jam yang dipilih, tampilkan semua jam
    if not selected_hours:
        selected_hours = range(0, 24)

    filtered_pattern = hourly_pattern[hourly_pattern['hr'].isin(selected_hours)]
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="hr", y="cnt", data=filtered_pattern, label="Total Penyewaan", color="blue")
    sns.lineplot(x="hr", y="casual", data=filtered_pattern, label="Casual", color="green")
    sns.lineplot(x="hr", y="registered", data=filtered_pattern, label="Registered", color="orange")

    # Menambahkan detail plot
    plt.title("Pola Rata-rata Penyewaan Sepeda per Jam", fontsize=14)
    plt.xlabel("Jam", fontsize=12)
    plt.ylabel("Rata-rata Penyewaan", fontsize=12)
    plt.xticks(range(min(selected_hours), max(selected_hours) + 1))
    plt.legend()
    plt.grid(alpha=0.3)
    st.pyplot(plt)

# Fungsi untuk plot faktor yang memengaruhi jumlah pengguna sepeda
def plot_factor_influence(correlation_data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=correlation_data.index, y=correlation_data.values)
    plt.title('Faktor yang Memengaruhi Jumlah Pengguna Sepeda')
    plt.xlabel('Faktor')
    plt.ylabel('Korelasi dengan Jumlah Pengguna')

    # Rotasi label sumbu x untuk kemudahan membaca
    plt.xticks(rotation=45, ha='right')  # Rotasi 45 derajat
    st.pyplot(plt)

# Judul
st.title('Dashboard Pola Penggunaan Sepeda :bar_chart:')

# Filter berdasarkan tanggal
st.sidebar.header('Filter Data')
start_date = st.sidebar.date_input('Mulai Tanggal', min_value=pd.to_datetime(data_day['dteday']).min(), max_value=pd.to_datetime(data_day['dteday']).max())
end_date = st.sidebar.date_input('Akhir Tanggal', min_value=start_date, max_value=pd.to_datetime(data_day['dteday']).max())

# Filter berdasarkan jam
hour_filter = st.sidebar.multiselect(
    'Pilih Jam',
    options=range(0, 24),
    default=range(0, 24),
    help="Pilih jam tertentu untuk menganalisis pola penyewaan sepeda berdasarkan jam."
)

# Filter data berdasarkan tanggal
filtered_data = data_day[(pd.to_datetime(data_day['dteday']) >= pd.to_datetime(start_date)) & (pd.to_datetime(data_day['dteday']) <= pd.to_datetime(end_date))]

# Pertanyaan 1: Pola Penggunaan Sepeda Berdasarkan Musim
season = filtered_data.groupby('season').agg({
    'cnt': ['mean', 'sum'],
    'casual': 'mean',
    'registered': 'mean'
}).reset_index()

# Tampilkan grafik pola penggunaan sepeda berdasarkan musim
st.subheader('Pola Penggunaan Sepeda Berdasarkan Musim')
plot_season_usage(season)

# Pertanyaan 2: Faktor yang Memengaruhi Jumlah Pengguna Sepeda
data_combined = pd.merge(filtered_data, data_hr, on='dteday', suffixes=('_day', '_hour'))
hourly_pattern = data_hr.groupby('hr')[['cnt', 'casual', 'registered']].mean().reset_index()

# Tampilkan grafik pola penyewaan sepeda berdasarkan jam
st.subheader('Pola Penggunaan Sepeda Berdasarkan Jam')
plot_hourly_usage(hourly_pattern, hour_filter)

# korelasi antara faktor-faktor yang memengaruhi jumlah pengguna sepeda
data_numerik = data_hr.select_dtypes(include=['float64', 'int64'])
korelasi = data_numerik.corr()
korelasi_cnt = korelasi['cnt'].sort_values(ascending=False)

# Tampilkan grafik faktor yang memengaruhi jumlah pengguna sepeda
st.subheader('Faktor yang Memengaruhi Jumlah Pengguna Sepeda')
plot_factor_influence(korelasi_cnt)


