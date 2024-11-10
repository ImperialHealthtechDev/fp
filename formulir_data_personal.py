import streamlit as st
import pandas as pd
import json
import io
from fpdf import FPDF


def formulir_data_personal():
    # Header dan pengantar
    st.header("Formulir Data Personal")
    st.write("""
        **Tentang Formulir Data Personal:**
        Formulir ini membantu Anda memulai perjalanan menuju kebebasan finansial. 
        Dengan mengisi data pribadi seperti pendapatan dan pengeluaran bulanan, Anda 
        dapat memperoleh wawasan mendalam tentang kondisi keuangan Anda saat ini.
        Data ini juga menjadi dasar untuk simulasi dan perhitungan finansial di fitur lainnya.
        
        **Manfaat Mengisi Formulir Ini:**
        - **Memahami Kesehatan Keuangan**: Dapatkan gambaran lengkap tentang keuangan Anda.
        - **Mendukung Perencanaan Keuangan Lainnya**: Data ini digunakan untuk simulasi dana pensiun, investasi, dan lainnya.
        - **Identifikasi Area Penghematan**: Temukan peluang untuk mengoptimalkan pengeluaran.
    """)

    # Form untuk input data personal
    with st.form("personal_form"):
        nama = st.text_input("Nama")
        tahun_lahir = st.number_input(
            "Tahun Kelahiran", min_value=1900, max_value=2024, step=1)
        pendapatan_bulanan = st.number_input(
            "Pendapatan Bulanan (Rp)", min_value=0, step=100000, format="%d")
        pengeluaran_bulanan = st.number_input(
            "Pengeluaran Bulanan (Rp)", min_value=0, step=100000, format="%d")

        # Tombol submit form
        submit_button = st.form_submit_button("Simpan Data")

    # Logika saat tombol submit ditekan
    if submit_button:
        st.success(f"Data berhasil disimpan untuk {nama}!")
        st.write(f"Tahun Kelahiran: {tahun_lahir}")
        st.write(f"Pendapatan Bulanan: Rp {pendapatan_bulanan:,}")
        st.write(f"Pengeluaran Bulanan: Rp {pengeluaran_bulanan:,}")

        # Menyimpan data ke dalam format JSON
        data_personal = {
            "Nama": nama,
            "Tahun Lahir": tahun_lahir,
            "Pendapatan Bulanan": pendapatan_bulanan,
            "Pengeluaran Bulanan": pengeluaran_bulanan
        }

        json_data = json.dumps(data_personal, indent=4)
        st.download_button(
            label="Ekspor Data FinPath (JSON)",
            data=json_data,
            file_name=f"{nama}_data_finpath.json",
            mime="application/json"
        )

        # Ekspor ke Excel
        df = pd.DataFrame([data_personal])
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Data Personal")
        st.download_button(
            label="Ekspor Data ke Excel",
            data=excel_buffer,
            file_name=f"{nama}_data_finpath.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Ekspor ke PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Data Personal - {nama}", ln=True, align='C')
        for key, value in data_personal.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

        # Konversi output PDF ke binary data
        pdf_output = pdf.output(dest='S').encode('latin1')

        st.download_button(
            label="Ekspor Data ke PDF",
            data=pdf_output,
            file_name=f"{nama}_data_finpath.pdf",
            mime="application/pdf"
        )

    # Fungsi unggah file JSON
    uploaded_file = st.sidebar.file_uploader(
        "Unggah Data FinPath (JSON)", type="json")
    if uploaded_file is not None:
        uploaded_data = json.load(uploaded_file)
        st.sidebar.success("Data berhasil diunggah!")
        st.sidebar.write("Data yang diunggah:")
        st.sidebar.json(uploaded_data)

    # Visualisasi data dalam bentuk grafik
    if submit_button:
        df_chart = pd.DataFrame({
            "Kategori": ["Pendapatan Bulanan", "Pengeluaran Bulanan"],
            "Jumlah (Rp)": [pendapatan_bulanan, pengeluaran_bulanan]
        })
        st.bar_chart(df_chart.set_index("Kategori"))
