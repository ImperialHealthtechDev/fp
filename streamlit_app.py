import streamlit as st
from formulir_data_personal import formulir_data_personal
from simulasi_dana_pensiun import simulasi_dana_pensiun
from kalkulator_investasi import kalkulator_investasi
from tracker_net_worth import tracker_net_worth
from rencana_anggaran import rencana_anggaran_bulanan
from dashboard_keuangan import dashboard_keuangan
from perencana_utang import perencana_pembayaran_utang
from simulasi_dana_darurat import simulasi_dana_darurat
from perencana_aset_besar import perencana_pembelian_aset_besar
from kalkulator_asuransi import kalkulator_asuransi_kebutuhan
from kalkulator_rencana_pendidikan import kalkulator_rencana_pendidikan_anak
from kalkulator_investasi_properti import kalkulator_kelayakan_investasi_properti

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="FinPath", layout="wide")

# Menu utama
menu_utama = st.sidebar.selectbox(
    "Pilih Kategori:",
    ["Home", "Data Personal", "Simulasi & Kalkulator",
        "Perencana Keuangan", "Tracker & Dashboard"]
)

# Sub-menu berdasarkan kategori
if menu_utama == "Home":
    st.title("FinPath - Your Path to Financial Freedom")
    st.write("Selamat datang di FinPath, aplikasi yang membantu Anda merencanakan dan mencapai kebebasan finansial.")
    st.write("Gunakan sidebar untuk menavigasi ke berbagai fitur.")

elif menu_utama == "Data Personal":
    submenu = st.sidebar.radio("Pilih Fitur Data Personal:", [
                               "Formulir Data Personal"])
    if submenu == "Formulir Data Personal":
        formulir_data_personal()

elif menu_utama == "Simulasi & Kalkulator":
    submenu = st.sidebar.radio("Pilih Fitur Simulasi & Kalkulator:", [
        "Simulasi Dana Pensiun", "Kalkulator Investasi Compound Interest", "Kalkulator Rencana Pendidikan Anak",
        "Kalkulator Kelayakan Investasi Properti", "Kalkulator Asuransi Kebutuhan"
    ])
    if submenu == "Simulasi Dana Pensiun":
        simulasi_dana_pensiun()
    elif submenu == "Kalkulator Investasi Compound Interest":
        kalkulator_investasi()
    elif submenu == "Kalkulator Rencana Pendidikan Anak":
        kalkulator_rencana_pendidikan_anak()
    elif submenu == "Kalkulator Kelayakan Investasi Properti":
        kalkulator_kelayakan_investasi_properti()
    elif submenu == "Kalkulator Asuransi Kebutuhan":
        kalkulator_asuransi_kebutuhan()

elif menu_utama == "Perencana Keuangan":
    submenu = st.sidebar.radio("Pilih Perencana Keuangan:", [
        "Rencana Anggaran Bulanan", "Perencana Pembayaran Utang", "Simulasi Dana Darurat", "Perencana Pembelian Aset Besar"
    ])
    if submenu == "Rencana Anggaran Bulanan":
        rencana_anggaran_bulanan()
    elif submenu == "Perencana Pembayaran Utang":
        perencana_pembayaran_utang()
    elif submenu == "Simulasi Dana Darurat":
        simulasi_dana_darurat()
    elif submenu == "Perencana Pembelian Aset Besar":
        perencana_pembelian_aset_besar()

elif menu_utama == "Tracker & Dashboard":
    submenu = st.sidebar.radio("Pilih Fitur Tracker & Dashboard:", [
                               "Tracker Net Worth", "Dashboard Keuangan"])
    if submenu == "Tracker Net Worth":
        tracker_net_worth()
    elif submenu == "Dashboard Keuangan":
        dashboard_keuangan()
