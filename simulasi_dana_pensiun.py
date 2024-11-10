import streamlit as st
import pandas as pd


def simulasi_dana_pensiun():
    st.header("Simulasi Dana Pensiun")
    st.write("Hitung berapa dana pensiun yang perlu Anda siapkan untuk masa depan.")

    with st.form("simulasi_pensiun_form"):
        pengeluaran_bulanan_pensiun = st.number_input(
            "Pengeluaran Bulanan di Masa Pensiun (Rp)", min_value=0, step=100000, format="%d")
        umur_sekarang = st.number_input(
            "Umur Saat Ini", min_value=18, max_value=100, step=1)
        umur_pensiun = st.number_input(
            "Umur Rencana Pensiun", min_value=umur_sekarang + 1, max_value=120, step=1)
        estimasi_inflasi = st.slider(
            "Estimasi Inflasi Tahunan (%)", min_value=0.0, max_value=10.0, value=3.0, step=0.1)
        return_investasi = st.slider(
            "Estimasi Return Investasi Tahunan (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1)

        submit_simulasi = st.form_submit_button("Hitung Dana Pensiun")

    if submit_simulasi:
        tahun_pensiun = umur_pensiun - umur_sekarang
        pengeluaran_tahunan = pengeluaran_bulanan_pensiun * 12
        future_pengeluaran_tahunan = pengeluaran_tahunan * \
            ((1 + estimasi_inflasi / 100) ** tahun_pensiun)
        total_dana_pensiun = future_pengeluaran_tahunan * 25

        st.subheader("Hasil Simulasi Dana Pensiun")
        st.write(
            f"Pengeluaran tahunan di masa pensiun: Rp {future_pengeluaran_tahunan:,.0f}")
        st.write(
            f"Total dana pensiun yang dibutuhkan (4% rule): Rp {total_dana_pensiun:,.0f}")

        st.line_chart(pd.DataFrame({
            "Umur": list(range(umur_sekarang, umur_pensiun + 1)),
            "Proyeksi Pengeluaran Tahunan (Rp)": [pengeluaran_tahunan * ((1 + estimasi_inflasi / 100) ** i) for i in range(0, tahun_pensiun + 1)]
        }).set_index("Umur"))
