import streamlit as st
import pandas as pd
import io
from fpdf import FPDF


def perencana_pembelian_aset_besar():
    st.title("Perencana Pembelian Aset Besar")
    st.write("Rencanakan pembelian aset besar seperti rumah, kendaraan, atau pendidikan anak dengan fitur ini.")

    # Form input untuk perencanaan pembelian aset
    with st.form("aset_besar_form"):
        harga_aset = st.number_input(
            "Harga Aset (Rp)", min_value=0, step=1000000, format="%d")
        waktu_beli = st.number_input(
            "Waktu Pembelian yang Diinginkan (dalam tahun)", min_value=1, step=1)
        tabungan_bulanan = st.number_input(
            "Alokasi Tabungan Bulanan (Rp)", min_value=0, step=100000, format="%d")
        estimasi_return_investasi = st.slider(
            "Estimasi Return Investasi Tahunan (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)

        submit_aset = st.form_submit_button("Hitung Rencana")

    if submit_aset:
        # Kalkulasi total tabungan tanpa investasi
        total_tabungan_tanpa_investasi = tabungan_bulanan * 12 * waktu_beli

        # Kalkulasi total tabungan dengan investasi (compound interest)
        total_tabungan_dengan_investasi = 0
        for tahun in range(1, waktu_beli + 1):
            total_tabungan_dengan_investasi += tabungan_bulanan * \
                12 * ((1 + estimasi_return_investasi / 100) ** tahun)

        # Menampilkan hasil
        st.subheader("Hasil Perhitungan")
        st.write(f"Harga Aset: Rp {harga_aset:,}")
        st.write(
            f"Total Tabungan Tanpa Investasi dalam {waktu_beli} tahun: Rp {total_tabungan_tanpa_investasi:,.0f}")
        st.write(
            f"Total Tabungan Dengan Investasi dalam {waktu_beli} tahun (estimasi {estimasi_return_investasi}% return tahunan): Rp {total_tabungan_dengan_investasi:,.0f}")

        if total_tabungan_dengan_investasi >= harga_aset:
            st.success(
                "Anda dapat mencapai target pembelian aset dengan strategi tabungan dan investasi ini!")
        elif total_tabungan_tanpa_investasi >= harga_aset:
            st.warning(
                "Anda dapat mencapai target pembelian aset dengan tabungan biasa, namun investasi dapat membantu mencapai target lebih cepat.")
        else:
            st.error("Jumlah tabungan saat ini tidak mencukupi untuk mencapai target pembelian aset. Pertimbangkan untuk meningkatkan alokasi tabungan atau jangka waktu.")

        # Ekspor data ke Excel
        data_aset = pd.DataFrame({
            "Jenis Rencana": ["Tanpa Investasi", "Dengan Investasi"],
            "Total Tabungan (Rp)": [total_tabungan_tanpa_investasi, total_tabungan_dengan_investasi]
        })

        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            data_aset.to_excel(writer, index=False, sheet_name="Rencana Aset")

        st.download_button(
            label="Ekspor Rencana ke Excel",
            data=excel_buffer,
            file_name="rencana_pembelian_aset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Ekspor data ke PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Laporan Rencana Pembelian Aset Besar",
                 ln=True, align='C')
        pdf.cell(200, 10, txt=f"Harga Aset: Rp {harga_aset:,}", ln=True)
        pdf.cell(
            200, 10, txt=f"Total Tabungan Tanpa Investasi: Rp {total_tabungan_tanpa_investasi:,.0f}", ln=True)
        pdf.cell(
            200, 10, txt=f"Total Tabungan Dengan Investasi: Rp {total_tabungan_dengan_investasi:,.0f}", ln=True)

        pdf_output = pdf.output(dest='S').encode('latin1')
        st.download_button(
            label="Ekspor Rencana ke PDF",
            data=pdf_output,
            file_name="rencana_pembelian_aset.pdf",
            mime="application/pdf"
        )
