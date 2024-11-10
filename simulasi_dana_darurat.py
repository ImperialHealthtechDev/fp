import streamlit as st


def simulasi_dana_darurat():
    st.title("Simulasi Dana Darurat")
    st.write("Alat ini membantu Anda menghitung berapa banyak dana darurat yang perlu disiapkan berdasarkan pengeluaran bulanan.")

    # Form input untuk pengeluaran bulanan dan jumlah bulan yang diinginkan
    with st.form("form_dana_darurat"):
        pengeluaran_bulanan = st.number_input(
            "Pengeluaran Bulanan (Rp)", min_value=0, step=100000, format="%d")
        jumlah_bulan = st.slider(
            "Jumlah Bulan untuk Dana Darurat", min_value=1, max_value=24, value=6, step=1)

        submit_darurat = st.form_submit_button("Hitung Dana Darurat")

    # Logika untuk perhitungan dana darurat
    if submit_darurat:
        total_dana_darurat = pengeluaran_bulanan * jumlah_bulan

        st.subheader("Hasil Simulasi Dana Darurat")
        st.write(
            f"Untuk menutupi pengeluaran selama {jumlah_bulan} bulan, dana darurat yang diperlukan adalah: **Rp {total_dana_darurat:,.0f}**")

        # Menampilkan peringatan motivasi jika jumlah bulan lebih besar dari 12
        if jumlah_bulan > 12:
            st.info("Anda telah memilih untuk mempersiapkan dana darurat lebih dari satu tahun. Ini adalah langkah yang sangat aman dan cerdas!")

        # Opsi untuk menampilkan rincian
        st.write("Rincian:")
        st.write(f"Pengeluaran Bulanan: Rp {pengeluaran_bulanan:,.0f}")
        st.write(f"Jumlah Bulan: {jumlah_bulan}")
        st.write(f"Total Dana Darurat: Rp {total_dana_darurat:,.0f}")
