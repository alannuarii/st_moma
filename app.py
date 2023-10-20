import streamlit as st
from model.prediction import mode_prediction

# SIDEBAR
# Icon
icon = "static/img/icon.png"
st.sidebar.image(icon, width=300)

# Input Data Uji
status = [0, 1, 2]
str_cuaca = [
    "Cerah",
    "Cerah Berawan",
    "Berawan",
    "Berawan Tebal",
    "Udara Kabur",
    "Asap",
    "Kabut",
    "Hujan Ringan",
    "Hujan Sedang",
    "Hujan Lebat",
    "Hujan Lokal",
    "Hujan Petir",
]

pv = st.sidebar.radio("Pilih Jumlah PV (Stand By)", status, horizontal=True)
bss = st.sidebar.radio("Pilih Jumlah BSS (Stand By)", status, horizontal=True)
dg = st.sidebar.radio("Pilih Jumlah DG / PLTD (Stand By)", status, horizontal=True)
cuaca = st.sidebar.selectbox("Pilih Kondisi Cuaca", str_cuaca)
irradiance = st.sidebar.number_input("Masukkan Nilai Irradiance (kWh)", min_value=0)

if(str_cuaca.index(cuaca) == 0 or str_cuaca.index(cuaca) == 1):
    kode_cuaca = 1
else:
    kode_cuaca = 0

if irradiance >= 700:
    kode_irr = 1
else: 
    kode_irr = 0


# MAIN
st.write(mode_prediction(pv, bss, dg, kode_cuaca, kode_irr))
