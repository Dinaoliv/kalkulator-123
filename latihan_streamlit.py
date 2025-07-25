# -*- coding: utf-8 -*-
"""latihan streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s7dk5-sCgYJu9D2q3RN_DVliSk0lZWZM
"""

import streamlit as st
import math
import time

st.set_page_config(page_title="Kalkulator Koordinat Kartesius", layout="wide")

# Sidebar Menu di Samping Kanan
st.sidebar.title("🔧 Menu Navigasi")
menu = st.sidebar.radio("Pilih Menu", ["📖 Panduan", "📍 Kalkulator Koordinat"])

# Halaman Panduan
if menu == "📖 Panduan":
    st.title("📖 Panduan Penggunaan")
    with st.expander("Lihat Petunjuk Lengkap"):
        st.write("""
        Selamat datang di Aplikasi Kalkulator Koordinat Kartesius!

        **Fitur:**
        - Hitung Jarak antara 2 titik di bidang koordinat.
        - Hitung Kemiringan garis yang menghubungkan kedua titik.

        **Langkah-langkah:**
        1️⃣ Pilih menu 'Kalkulator Koordinat'.
        2️⃣ Masukkan koordinat (X1, Y1) dan (X2, Y2).
        3️⃣ Klik tombol *Hitung*, tunggu proses selesai.
        4️⃣ Lihat hasil jarak dan kemiringan yang tampil.

        **Catatan:**
        Untuk garis vertikal, kemiringan dianggap *Tak Hingga*.
        """)

# Halaman Kalkulator Koordinat
elif menu == "📍 Kalkulator Koordinat":
    st.title("📍 Kalkulator Koordinat Kartesius Interaktif")
    st.write("Masukkan koordinat dua titik untuk mengetahui jarak dan kemiringan garis:")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Titik Pertama - X1", value=0.0, step=0.1)
        y1 = st.number_input("Titik Pertama - Y1", value=0.0, step=0.1)

    with col2:
        x2 = st.number_input("Titik Kedua - X2", value=0.0, step=0.1)
        y2 = st.number_input("Titik Kedua - Y2", value=0.0, step=0.1)

    st.markdown("---")

    if st.button("🚀 Hitung Jarak & Kemiringan"):
        with st.spinner("Sedang menghitung..."):
            time.sleep(1)  # simulasi proses

            jarak = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if x2 - x1 != 0:
                kemiringan = (y2 - y1) / (x2 - x1)
                kemiringan_text = f"{kemiringan:.2f}"
            else:
                kemiringan_text = "Tak Hingga (Garis Vertikal)"

            st.success("✅ Perhitungan Selesai!")

            st.metric("Jarak antara dua titik", f"{jarak:.2f}")
            st.metric("Kemiringan garis", kemiringan_text)