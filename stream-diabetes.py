import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Prediksi Data Mining Diabetes')

#membagi kolom
col1,col2=st.columns(2)

with col1:
    Pregnancies = st.text_input('Masukkan nilai Pregnancies')
with col2:
    Gula = st.text_input('Masukkan nilai Gula')
with col1:
    TekananDarah = st.text_input('Masukkan nilai Tekanan Darah')
with col2:
    KetebalanKulit = st.text_input('Masukkan nilai Ketebalan Kulit')
with col1:
    Insulin = st.text_input('Masukkan nilai Insulin')
with col2:
    BMI = st.text_input('Masukkan nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Masukkan nilai Diabetes Pedigree  Function')
with col2:
    Umur = st.text_input('Masukkan nilai Umur')

# Kode untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Gula, TekananDarah, KetebalanKulit, Insulin, BMI,
                                               DiabetesPedigreeFunction, Umur]])

    if (diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

# Memastikan st.success(diab_diagnosis) berada di luar blok if
st.success(diab_diagnosis)
