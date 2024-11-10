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

# Konfigurasi halaman Streamlit harus berada di atas
st.set_page_config(page_title="FinPath", layout="wide")

# Tambahkan CSS untuk efek hover dan highlight menu
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 300px;
    }
    .stButton > button {
        width: 100%;
        margin-bottom: 5px;
    }
    .stButton:hover > button {
        background-color: #f0f0f0;
    }
    .highlighted > button {
        background-color: #FF4B4B !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar dengan expander dan highlight menu aktif
selected_menu = ""

with st.sidebar:
    st.header("Navigasi")

    with st.expander("Perencanaan Keuangan", expanded=True):
        if st.button("Formulir Data Personal", key="form_data"):
            selected_menu = "Formulir Data Personal"
        if st.button("Rencana Anggaran Bulanan", key="rencana_anggaran"):
            selected_menu = "Rencana Anggaran Bulanan"
        if st.button("Simulasi Dana Pensiun", key="simulasi_pensiun"):
            selected_menu = "Simulasi Dana Pensiun"
        if st.button("Simulasi Dana Darurat", key="simulasi_darurat"):
            selected_menu = "Simulasi Dana Darurat"
        if st.button("Dashboard Keuangan", key="dashboard"):
            selected_menu = "Dashboard Keuangan"

    with st.expander("Investasi dan Pengelolaan Aset", expanded=False):
        if st.button("Kalkulator Investasi Compound Interest", key="compound_interest"):
            selected_menu = "Kalkulator Investasi Compound Interest"
        if st.button("Tracker Net Worth", key="tracker_net_worth"):
            selected_menu = "Tracker Net Worth"
        if st.button("Perencana Pembelian Aset Besar", key="aset_besar"):
            selected_menu = "Perencana Pembelian Aset Besar"
        if st.button("Kalkulator Kelayakan Investasi Properti", key="investasi_properti"):
            selected_menu = "Kalkulator Kelayakan Investasi Properti"

    with st.expander("Asuransi dan Pendidikan", expanded=False):
        if st.button("Kalkulator Asuransi Kebutuhan", key="asuransi_kebutuhan"):
            selected_menu = "Kalkulator Asuransi Kebutuhan"
        if st.button("Kalkulator Rencana Pendidikan Anak", key="rencana_pendidikan"):
            selected_menu = "Kalkulator Rencana Pendidikan Anak"

# Highlight menu aktif
if selected_menu:
    st.markdown(
        f"""
        <script>
        document.querySelectorAll('button').forEach(button => {{
            if (button.textContent === '{selected_menu}') {{
                button.parentElement.classList.add('highlighted');
            }}
        }});
        </script>
        """,
        unsafe_allow_html=True
    )

# Panggil fungsi berdasarkan menu yang dipilih
if selected_menu == "Formulir Data Personal":
    formulir_data_personal()
elif selected_menu == "Rencana Anggaran Bulanan":
    rencana_anggaran_bulanan()
elif selected_menu == "Simulasi Dana Pensiun":
    simulasi_dana_pensiun()
elif selected_menu == "Simulasi Dana Darurat":
    simulasi_dana_darurat()
elif selected_menu == "Dashboard Keuangan":
    dashboard_keuangan()
elif selected_menu == "Kalkulator Investasi Compound Interest":
    kalkulator_investasi()
elif selected_menu == "Tracker Net Worth":
    tracker_net_worth()
elif selected_menu == "Perencana Pembelian Aset Besar":
    perencana_pembelian_aset_besar()
elif selected_menu == "Kalkulator Asuransi Kebutuhan":
    kalkulator_asuransi_kebutuhan()
elif selected_menu == "Kalkulator Rencana Pendidikan Anak":
    kalkulator_rencana_pendidikan_anak()
elif selected_menu == "Kalkulator Kelayakan Investasi Properti":
    kalkulator_kelayakan_investasi_properti()

# Halaman utama jika tidak ada yang dipilih
if selected_menu == "":
    st.title("FinPath - Your Path to Financial Freedom")
    st.write("Selamat datang di FinPath, aplikasi yang membantu Anda merencanakan dan mencapai kebebasan finansial.")
    st.write("Gunakan sidebar untuk menavigasi ke berbagai fitur.")
