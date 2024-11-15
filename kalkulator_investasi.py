import streamlit as st


def kalkulator_investasi():
    st.title("Kalkulator Investasi Compound Interest")
    st.write("""
        **Tentang Kalkulator Investasi Compound Interest**  
        Alat ini dirancang untuk membantu Anda menghitung potensi pertumbuhan investasi Anda dari waktu ke waktu dengan metode bunga majemuk. Dengan kalkulator ini, Anda dapat memperkirakan seberapa besar investasi Anda akan berkembang jika Anda menambahkan kontribusi secara rutin dan mempertahankan tingkat pengembalian tertentu.

        ### Manfaat Menggunakan Kalkulator Ini:
        - **Simulasi Pertumbuhan Investasi**: Membantu Anda memahami bagaimana kontribusi bulanan dan tingkat pengembalian tahunan memengaruhi hasil akhir.
        - **Perencanaan Jangka Panjang**: Memberikan gambaran tentang total investasi yang dapat dicapai dalam jangka waktu yang diinginkan.
        - **Keputusan Finansial yang Lebih Baik**: Mempermudah perencanaan keuangan dan penentuan strategi investasi untuk mencapai tujuan finansial Anda.
    """)

    with st.form("kalkulator_form"):
        investasi_awal = st.number_input(
            "Investasi Awal (Rp)", min_value=0, step=100000, format="%d")
        kontribusi_bulanan = st.number_input(
            "Kontribusi Bulanan (Rp)", min_value=0, step=100000, format="%d")
        tingkat_bunga = st.slider(
            "Tingkat Bunga Tahunan (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
        jangka_waktu = st.number_input(
            "Jangka Waktu (tahun)", min_value=1, max_value=50, step=1)

        submit_kalkulator = st.form_submit_button("Hitung")

    if submit_kalkulator:
        total = investasi_awal
        bunga_bulanan = (1 + tingkat_bunga / 100) ** (1 / 12) - 1
        total_akhir = []

        for bulan in range(1, jangka_waktu * 12 + 1):
            total += kontribusi_bulanan
            total *= (1 + bunga_bulanan)
            if bulan % 12 == 0:
                total_akhir.append(total)

        st.subheader("Hasil Simulasi Investasi")
        st.write(
            f"Total nilai investasi setelah {jangka_waktu} tahun: Rp {total:,.0f}")

        # Menampilkan grafik pertumbuhan investasi
        st.line_chart(total_akhir)
