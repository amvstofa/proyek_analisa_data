#Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip freeze > requirements.txt

#Run steamlit app
streamlit run dashboard/dashboard.py

# Dashboard Pola Penggunaan Sepeda

Aplikasi dashboard ini dibuat menggunakan Streamlit untuk menganalisis pola penggunaan sepeda berdasarkan data penyewaan sepeda dari berbagai sumber. Dengan aplikasi ini, pengguna dapat menjelajahi data dan membuat analisis interaktif mengenai penyewaan sepeda berdasarkan musim, jam, dan faktor-faktor lainnya.

## Fitur

1. **Pola Penggunaan Sepeda Berdasarkan Musim**:
   - Menampilkan rata-rata penyewaan sepeda untuk setiap musim (Winter, Spring, Summer, Fall).
2. **Pola Penggunaan Sepeda Berdasarkan Jam**:

   - Menampilkan pola penyewaan sepeda berdasarkan jam dan memungkinkan pengguna memilih jam tertentu yang ingin dianalisis.

3. **Faktor yang Memengaruhi Jumlah Pengguna Sepeda**:

   - Menampilkan faktor-faktor yang memiliki korelasi signifikan dengan jumlah pengguna sepeda.

4. **Filter Data**:
   - Pengguna dapat memfilter data berdasarkan rentang tanggal tertentu dan memilih jam yang diinginkan untuk analisis.

## Struktur File

- **dashboard.py**: Aplikasi Streamlit yang menjalankan dashboard interaktif.
- **day.csv**: Data harian penyewaan sepeda.
- **hour.csv**: Data penyewaan sepeda berdasarkan jam.
