import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def dashboard_keuangan():
    # Header dan pengantar
    st.title("Dashboard Keuangan")
    st.write("""
        **Selamat datang di Dashboard Keuangan Anda!**
        Dashboard ini memberikan ikhtisar lengkap tentang keuangan Anda, mulai dari pendapatan, pengeluaran, hingga net worth. 
        Lihat bagaimana kondisi keuangan Anda saat ini, pantau progres dana pensiun, dan evaluasi distribusi pengeluaran.
    """)

    # Input data keuangan
    pendapatan_bulanan = st.number_input(
        "Pendapatan Bulanan (Rp)", min_value=0, step=100000, format="%d", value=10000000)
    pengeluaran_bulanan = st.number_input(
        "Pengeluaran Bulanan (Rp)", min_value=0, step=100000, format="%d", value=5000000)
    total_aset = st.number_input(
        "Total Aset (Rp)", min_value=0, step=100000, format="%d", value=100000000)
    total_kewajiban = st.number_input(
        "Total Kewajiban (Rp)", min_value=0, step=100000, format="%d", value=20000000)

    # Menghitung net worth
    net_worth = total_aset - total_kewajiban

    # Menampilkan ringkasan dalam angka
    st.subheader("Ringkasan Keuangan")
    st.write(f"**Pendapatan Bulanan**: Rp {pendapatan_bulanan:,}")
    st.write(f"**Pengeluaran Bulanan**: Rp {pengeluaran_bulanan:,}")
    st.write(f"**Total Aset**: Rp {total_aset:,}")
    st.write(f"**Total Kewajiban**: Rp {total_kewajiban:,}")
    st.write(f"**Net Worth**: Rp {net_worth:,}")

    # Menampilkan peringatan jika net worth negatif
    if net_worth < 0:
        st.error(
            "Net worth Anda negatif. Perlu ditinjau ulang pengeluaran atau aset Anda.")
        st.write(
            "**Tips**: Pertimbangkan untuk mengurangi pengeluaran atau meningkatkan pendapatan Anda.")
    else:
        st.success("Net worth Anda positif. Keuangan Anda dalam kondisi baik.")
        st.write(
            "**Tips**: Pertahankan pengelolaan keuangan ini dan pertimbangkan investasi jangka panjang.")

    # Visualisasi pie chart distribusi pengeluaran
    st.subheader("Distribusi Pengeluaran")
    data_pengeluaran = {
        "Kategori": ["Pendapatan", "Pengeluaran"],
        "Jumlah (Rp)": [pendapatan_bulanan, pengeluaran_bulanan]
    }
    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    fig, ax = plt.subplots()
    colors = ["#66b3ff", "#ff9999"]
    ax.pie(df_pengeluaran["Jumlah (Rp)"],
           labels=df_pengeluaran["Kategori"], autopct='%1.1f%%', colors=colors)
    ax.axis('equal')  # Membuat pie chart berbentuk lingkaran
    st.pyplot(fig)

    # Progres dana pensiun
    st.subheader("Progres Dana Pensiun")
    target_dana_pensiun = st.number_input(
        "Target Dana Pensiun (Rp)", min_value=0, step=100000, format="%d", value=500000000)
    progres_dana_pensiun = (net_worth / target_dana_pensiun) * 100

    if progres_dana_pensiun > 100:
        progres_dana_pensiun = 100

    st.progress(progres_dana_pensiun / 100)
    st.write(f"Progres Dana Pensiun Anda: {progres_dana_pensiun:.2f}%")

    # Menampilkan ringkasan grafik pendapatan dan pengeluaran
    st.subheader("Grafik Pendapatan vs Pengeluaran")
    df_ringkasan = pd.DataFrame({
        "Kategori": ["Pendapatan", "Pengeluaran"],
        "Jumlah (Rp)": [pendapatan_bulanan, pengeluaran_bulanan]
    })
    st.bar_chart(df_ringkasan.set_index("Kategori"))
