import streamlit as st
import pandas as pd


def kalkulator_rencana_pendidikan_anak():
    st.title("Kalkulator Rencana Pendidikan Anak")
    st.write("""
        **Tentang Kalkulator Rencana Pendidikan Anak**  
        Alat ini dirancang untuk membantu Anda merencanakan dan menghitung berapa biaya pendidikan yang perlu Anda siapkan untuk anak Anda, dengan mempertimbangkan tingkat inflasi dan jangka waktu hingga masuk ke jenjang pendidikan tertentu.

        ### Manfaat Menggunakan Kalkulator Ini:
        - **Perencanaan Keuangan yang Lebih Matang**: Mempermudah Anda memahami biaya yang akan datang dan mempersiapkan tabungan/investasi yang tepat.
        - **Estimasi Proyeksi Biaya Pendidikan**: Menghitung proyeksi biaya di masa depan berdasarkan tingkat inflasi pendidikan.
        - **Strategi Tabungan/Investasi**: Memberikan saran mengenai jumlah tabungan bulanan atau investasi yang dibutuhkan untuk mencapai target.
    """)

    # Form input untuk data pendidikan anak
    with st.form("pendidikan_form"):
        usia_anak = st.number_input(
            "Usia Anak Saat Ini (tahun)", min_value=0, max_value=18, step=1)
        tingkat_pendidikan = st.selectbox("Tingkat Pendidikan Tertinggi yang Diinginkan",
                                          ["SD", "SMP", "SMA", "Universitas"])
        biaya_sekarang = st.number_input(
            "Biaya Pendidikan Saat Ini (Rp)", min_value=0, step=1000000, format="%d")
        inflasi_pendidikan = st.slider(
            "Tingkat Inflasi Pendidikan Tahunan (%)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)

        submit_pendidikan = st.form_submit_button("Hitung Rencana Pendidikan")

    if submit_pendidikan:
        # Mapping usia pendidikan berdasarkan tingkat pendidikan
        usia_masuk_pendidikan = {
            "SD": 6,
            "SMP": 12,
            "SMA": 15,
            "Universitas": 18
        }

        tahun_masuk = usia_masuk_pendidikan[tingkat_pendidikan] - usia_anak
        if tahun_masuk < 0:
            st.error(
                "Anak Anda telah melewati usia masuk untuk tingkat pendidikan ini.")
            return

        # Menghitung proyeksi biaya pendidikan
        proyeksi_biaya_pendidikan = biaya_sekarang * \
            ((1 + inflasi_pendidikan / 100) ** tahun_masuk)

        # Menampilkan hasil proyeksi
        st.subheader("Hasil Proyeksi Biaya Pendidikan")
        st.write(f"Tingkat pendidikan yang diinginkan: {tingkat_pendidikan}")
        st.write(
            f"Estimasi biaya pendidikan saat anak masuk {tingkat_pendidikan}: Rp {proyeksi_biaya_pendidikan:,.0f}")

        # Saran tabungan atau investasi
        st.subheader("Saran Tabungan atau Investasi")
        st.write(f"Untuk mengumpulkan Rp {proyeksi_biaya_pendidikan:,.0f} dalam {tahun_masuk} tahun, "
                 f"Anda perlu menabung atau menginvestasikan secara berkala.")

        # Estimasi tabungan bulanan
        bunga_investasi = st.slider(
            "Estimasi Return Investasi Tahunan (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1)
        jumlah_bulanan = proyeksi_biaya_pendidikan / \
            (((1 + bunga_investasi / 100) ** tahun_masuk - 1) /
             (bunga_investasi / 100) / 12)

        st.write(
            f"Anda perlu menabung sekitar Rp {jumlah_bulanan:,.0f} per bulan.")
