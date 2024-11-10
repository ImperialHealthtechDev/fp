import streamlit as st
import pandas as pd


def kalkulator_kelayakan_investasi_properti():
    st.title("Kalkulator Kelayakan Investasi Properti")
    st.write("Gunakan alat ini untuk mengevaluasi apakah investasi properti layak berdasarkan biaya dan potensi penghasilan.")

    # Form input untuk data investasi properti
    with st.form("investasi_properti_form"):
        harga_properti = st.number_input(
            "Harga Properti (Rp)", min_value=0, step=1000000, format="%d")
        biaya_perawatan_tahunan = st.number_input(
            "Biaya Perawatan Tahunan (Rp)", min_value=0, step=100000, format="%d")
        potensi_sewa_bulanan = st.number_input(
            "Potensi Penghasilan Sewa Bulanan (Rp)", min_value=0, step=100000, format="%d")
        biaya_lainnya_tahunan = st.number_input(
            "Biaya Lainnya Tahunan (Rp)", min_value=0, step=100000, format="%d")
        submit_properti = st.form_submit_button("Hitung Kelayakan Investasi")

    if submit_properti:
        # Menghitung ROI (Return on Investment)
        total_penghasilan_tahunan = potensi_sewa_bulanan * 12
        total_biaya_tahunan = biaya_perawatan_tahunan + biaya_lainnya_tahunan
        net_penghasilan_tahunan = total_penghasilan_tahunan - total_biaya_tahunan
        roi = (net_penghasilan_tahunan / harga_properti) * \
            100 if harga_properti > 0 else 0

        # Menampilkan hasil
        st.subheader("Hasil Kalkulasi Investasi Properti")
        st.write(
            f"Total Penghasilan Tahunan: Rp {total_penghasilan_tahunan:,.0f}")
        st.write(f"Total Biaya Tahunan: Rp {total_biaya_tahunan:,.0f}")
        st.write(f"Net Penghasilan Tahunan: Rp {net_penghasilan_tahunan:,.0f}")
        st.write(f"Return on Investment (ROI): {roi:.2f}%")

        # Analisis kelayakan
        if roi > 5:  # Ambang batas ROI 5% sebagai contoh
            st.success("Investasi properti ini layak dipertimbangkan.")
        else:
            st.warning(
                "Investasi properti ini mungkin kurang menguntungkan. Pertimbangkan opsi investasi lain.")

        # Menampilkan tabel ringkasan
        data_ringkasan = pd.DataFrame({
            "Item": ["Total Penghasilan Tahunan", "Total Biaya Tahunan", "Net Penghasilan Tahunan", "ROI (%)"],
            "Jumlah (Rp)": [total_penghasilan_tahunan, total_biaya_tahunan, net_penghasilan_tahunan, roi]
        })

        st.table(data_ringkasan)
