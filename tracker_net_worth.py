import streamlit as st
import pandas as pd
import io
from fpdf import FPDF
import os


def tracker_net_worth():
    st.title("Tracker Net Worth")
    st.write("""
        **Tentang Tracker Net Worth**  
        Alat ini membantu Anda mencatat dan memantau total kekayaan bersih Anda dari waktu ke waktu. Dengan melacak aset dan kewajiban secara berkala, Anda bisa mengukur kesehatan finansial Anda dan membuat perencanaan yang lebih baik.

        ### Manfaat Menggunakan Fitur Ini:
        - **Visualisasi Tren Keuangan**: Memantau tren kenaikan atau penurunan kekayaan bersih Anda dari waktu ke waktu.
        - **Pengambilan Keputusan Finansial yang Lebih Baik**: Informasi yang akurat membantu Anda membuat keputusan keuangan yang lebih bijaksana.
        - **Konsolidasi Data Keuangan**: Menyimpan dan mengelola data kekayaan bersih Anda dalam satu tempat yang aman.
    """)

    # Path file untuk menyimpan data CSV
    file_path = "net_worth_data.csv"

    # Membaca data dari file CSV jika ada
    if os.path.exists(file_path):
        data_net_worth = pd.read_csv(file_path)
    else:
        data_net_worth = pd.DataFrame(
            columns=['Tanggal', 'Aset (Rp)', 'Kewajiban (Rp)', 'Net Worth (Rp)'])

    # Input untuk aset dan kewajiban
    with st.form("net_worth_form"):
        aset = st.number_input(
            "Total Aset (Rp)", min_value=0, step=100000, format="%d")
        kewajiban = st.number_input(
            "Total Kewajiban (Rp)", min_value=0, step=100000, format="%d")
        tanggal = st.date_input("Tanggal")

        submit_button = st.form_submit_button("Simpan Data")

    # Logika untuk menyimpan dan menampilkan data
    if submit_button:
        net_worth = aset - kewajiban
        st.success(
            f"Data berhasil disimpan! Kekayaan bersih Anda: Rp {net_worth:,}")

        # Menambahkan data baru ke DataFrame
        new_data = pd.DataFrame({
            'Tanggal': [tanggal],
            'Aset (Rp)': [aset],
            'Kewajiban (Rp)': [kewajiban],
            'Net Worth (Rp)': [net_worth]
        })
        data_net_worth = pd.concat(
            [data_net_worth, new_data], ignore_index=True)

        # Menyimpan data ke file CSV
        data_net_worth.to_csv(file_path, index=False)

        # Tampilkan data
        st.write("Riwayat Net Worth:")
        st.dataframe(data_net_worth)

        # Visualisasi tren net worth
        st.subheader("Tren Net Worth Anda")
        st.line_chart(data_net_worth.set_index('Tanggal')['Net Worth (Rp)'])

        # Ekspor data ke Excel
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            data_net_worth.to_excel(
                writer, index=False, sheet_name="Net Worth Tracker")
        st.download_button(
            label="Ekspor Data ke Excel",
            data=excel_buffer,
            file_name="net_worth_tracker.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Ekspor data ke PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Laporan Net Worth Tracker", ln=True, align='C')
        for index, row in data_net_worth.iterrows():
            pdf.cell(
                200, 10, txt=f"{row['Tanggal']} - Aset: Rp {row['Aset (Rp)']:,}, Kewajiban: Rp {row['Kewajiban (Rp)']:,}, Net Worth: Rp {row['Net Worth (Rp)']:,}", ln=True)

        pdf_output = pdf.output(dest='S').encode('latin1')
        st.download_button(
            label="Ekspor Data ke PDF",
            data=pdf_output,
            file_name="net_worth_tracker.pdf",
            mime="application/pdf"
        )
