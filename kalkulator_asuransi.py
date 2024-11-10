import streamlit as st


def kalkulator_asuransi_kebutuhan():
    st.title("Kalkulator Asuransi Kebutuhan")
    st.write("Fitur ini membantu Anda menentukan jenis dan jumlah perlindungan asuransi yang dibutuhkan.")

    # Form input untuk kondisi keuangan dan risiko finansial
    with st.form("asuransi_form"):
        pendapatan_tahunan = st.number_input(
            "Pendapatan Tahunan (Rp)", min_value=0, step=1000000, format="%d")
        pengeluaran_tahunan = st.number_input(
            "Pengeluaran Tahunan (Rp)", min_value=0, step=1000000, format="%d")
        total_hutang = st.number_input(
            "Total Hutang (Rp)", min_value=0, step=1000000, format="%d")
        aset_likuid = st.number_input(
            "Total Aset Likuid (Rp)", min_value=0, step=1000000, format="%d")
        jumlah_tanggungan = st.number_input(
            "Jumlah Tanggungan (orang)", min_value=0, step=1)

        submit_asuransi = st.form_submit_button("Hitung Kebutuhan Asuransi")

    # Logika perhitungan kebutuhan asuransi
    if submit_asuransi:
        # Estimasi kebutuhan asuransi jiwa (contoh: 10x pendapatan tahunan)
        estimasi_asuransi_jiwa = pendapatan_tahunan * 10

        # Estimasi kebutuhan asuransi kesehatan dan properti
        estimasi_asuransi_kesehatan = pengeluaran_tahunan * \
            0.2  # Contoh: 20% dari pengeluaran tahunan
        estimasi_asuransi_properti = aset_likuid * 0.5  # Contoh: 50% dari aset likuid

        # Total estimasi perlindungan yang disarankan
        total_estimasi_perlindungan = estimasi_asuransi_jiwa + \
            estimasi_asuransi_kesehatan + estimasi_asuransi_properti

        # Menampilkan hasil perhitungan
        st.subheader("Rekomendasi Kebutuhan Asuransi")
        st.write(
            f"Estimasi perlindungan asuransi jiwa: Rp {estimasi_asuransi_jiwa:,.0f}")
        st.write(
            f"Estimasi perlindungan asuransi kesehatan: Rp {estimasi_asuransi_kesehatan:,.0f}")
        st.write(
            f"Estimasi perlindungan asuransi properti: Rp {estimasi_asuransi_properti:,.0f}")
        st.write(
            f"Total nilai perlindungan yang disarankan: Rp {total_estimasi_perlindungan:,.0f}")

        # Rekomendasi tambahan
        st.info("Rekomendasi: Pastikan untuk menyesuaikan perlindungan asuransi dengan kondisi keuangan dan kebutuhan pribadi Anda.")