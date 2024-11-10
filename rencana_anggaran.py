import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
from fpdf import FPDF


def rencana_anggaran_bulanan():
    st.title("Rencana Anggaran Bulanan")
    st.write("Gunakan alat ini untuk merencanakan dan melacak anggaran bulanan Anda.")

    # Form input untuk anggaran berbagai kategori
    with st.form("anggaran_form"):
        pendapatan_bulanan = st.number_input(
            "Pendapatan Bulanan (Rp)", min_value=0, step=100000, format="%d")
        makanan = st.number_input(
            "Anggaran Makanan (Rp)", min_value=0, step=50000, format="%d")
        transportasi = st.number_input(
            "Anggaran Transportasi (Rp)", min_value=0, step=50000, format="%d")
        hiburan = st.number_input(
            "Anggaran Hiburan (Rp)", min_value=0, step=50000, format="%d")
        lainnya = st.number_input(
            "Anggaran Lainnya (Rp)", min_value=0, step=50000, format="%d")

        submit_anggaran = st.form_submit_button("Simpan Anggaran")

    # Logika untuk menampilkan hasil setelah submit
    if submit_anggaran:
        total_anggaran = makanan + transportasi + hiburan + lainnya
        sisa_anggaran = pendapatan_bulanan - total_anggaran

        st.subheader("Ringkasan Anggaran")
        st.write(f"Pendapatan Bulanan: Rp {pendapatan_bulanan:,}")
        st.write(f"Total Pengeluaran: Rp {total_anggaran:,}")
        st.write(f"Sisa Anggaran: Rp {sisa_anggaran:,}")

        # Menampilkan peringatan jika total pengeluaran melebihi pendapatan
        if sisa_anggaran < 0:
            st.error(
                "Total pengeluaran melebihi pendapatan. Harap tinjau kembali anggaran Anda.")
        else:
            st.success("Anggaran Anda seimbang atau memiliki sisa.")

        # Membuat DataFrame untuk visualisasi
        data_anggaran = pd.DataFrame({
            "Kategori": ["Makanan", "Transportasi", "Hiburan", "Lainnya"],
            "Jumlah (Rp)": [makanan, transportasi, hiburan, lainnya]
        })

        # Menampilkan pie chart distribusi pengeluaran
        st.subheader("Distribusi Pengeluaran")
        fig, ax = plt.subplots()
        ax.pie(data_anggaran["Jumlah (Rp)"],
               labels=data_anggaran["Kategori"], autopct='%1.1f%%')
        ax.axis('equal')  # Untuk membuat pie chart berbentuk lingkaran
        st.pyplot(fig)

        # Ekspor data ke Excel
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            data_anggaran.to_excel(writer, index=False,
                                   sheet_name="Rencana Anggaran")
        st.download_button(
            label="Ekspor Anggaran ke Excel",
            data=excel_buffer,
            file_name="rencana_anggaran.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Ekspor data ke PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Laporan Rencana Anggaran Bulanan",
                 ln=True, align='C')
        pdf.cell(
            200, 10, txt=f"Pendapatan Bulanan: Rp {pendapatan_bulanan:,}", ln=True)
        pdf.cell(
            200, 10, txt=f"Total Pengeluaran: Rp {total_anggaran:,}", ln=True)
        pdf.cell(200, 10, txt=f"Sisa Anggaran: Rp {sisa_anggaran:,}", ln=True)
        pdf.cell(200, 10, txt="Rincian Pengeluaran:", ln=True)
        for index, row in data_anggaran.iterrows():
            pdf.cell(
                200, 10, txt=f"{row['Kategori']}: Rp {row['Jumlah (Rp)']:,}", ln=True)

        pdf_output = pdf.output(dest='S').encode('latin1')
        st.download_button(
            label="Ekspor Anggaran ke PDF",
            data=pdf_output,
            file_name="rencana_anggaran.pdf",
            mime="application/pdf"
        )
