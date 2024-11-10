import streamlit as st
import pandas as pd


def perencana_pembayaran_utang():
    st.title("Perencana Pembayaran Utang - Debt Snowball Calculator")
    st.write(
        "Gunakan alat ini untuk merencanakan pembayaran utang Anda dengan metode debt snowball.")

    # Input data utang
    st.subheader("Masukkan Data Utang")
    data_utang = []

    with st.form("form_utang"):
        num_debts = st.number_input(
            "Jumlah Utang yang Ingin Dimasukkan", min_value=1, step=1, value=1)

        for i in range(num_debts):
            st.write(f"Utang {i + 1}")
            jumlah_utang = st.number_input(
                f"Jumlah Utang {i + 1} (Rp)", min_value=0, step=100000, format="%d", key=f"jumlah_{i}")
            bunga_utang = st.number_input(
                f"Bunga Tahunan (%) Utang {i + 1}", min_value=0.0, max_value=100.0, step=0.1, key=f"bunga_{i}")
            pembayaran_minimum = st.number_input(
                f"Pembayaran Minimum (Rp) Utang {i + 1}", min_value=0, step=10000, format="%d", key=f"pembayaran_{i}")

            data_utang.append({
                "Utang": f"Utang {i + 1}",
                "Jumlah Utang": jumlah_utang,
                "Bunga (%)": bunga_utang,
                "Pembayaran Minimum": pembayaran_minimum
            })

        submit_utang = st.form_submit_button("Simpan Data Utang")

    if submit_utang:
        df_utang = pd.DataFrame(data_utang)
        st.subheader("Rincian Utang Anda")
        st.dataframe(df_utang)

        # Mengurutkan utang berdasarkan jumlah terkecil ke terbesar (metode snowball)
        df_utang = df_utang.sort_values(by="Jumlah Utang")

        st.subheader("Rencana Pembayaran (Metode Debt Snowball)")
        st.write("Rencana pembayaran dimulai dari utang terkecil ke terbesar:")

        total_pembayaran = 0
        for index, row in df_utang.iterrows():
            total_pembayaran += row["Jumlah Utang"]
            st.write(
                f"Mulai melunasi **{row['Utang']}** dengan jumlah Rp {row['Jumlah Utang']:,}.")

        st.write("Total estimasi pembayaran untuk melunasi semua utang: Rp {:,}".format(
            total_pembayaran))

        # Menampilkan progress rencana pembayaran
        st.progress(1.0)

        # Ekspor data utang ke Excel
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df_utang.to_excel(writer, index=False,
                              sheet_name="Rencana Pembayaran Utang")
        st.download_button(
            label="Ekspor Rencana Pembayaran ke Excel",
            data=excel_buffer,
            file_name="rencana_pembayaran_utang.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Menampilkan ringkasan untuk motivasi pengguna
        st.success(
            "Selamat! Anda memiliki rencana untuk melunasi utang dengan metode debt snowball.")
