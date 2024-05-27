import streamlit as st
import models.Forecast as forecast
import services.database as db

def run(username):
    
    st.header(':heavy_plus_sign: Cadastro de Previsão')

    with st.form(key = 'input_forescast'):

        input_username = username
        input_supp_code = st.text_input(label='Insira o código do fornecedor')
        input_year = st.number_input(label= 'Insira o ano', step = 1)
        input_month = st.selectbox('Selecione o mês', list(range(1, 13)))
        input_price = st.number_input('Insira o valor unitário (U$)')
        input_vol = st.number_input('Insira o volume (un.)')
        input_btn_submit = st.form_submit_button('Cadastrar')

    if input_btn_submit:

        forecast.user = input_username
        forecast.year = input_year
        forecast.month = input_month
        forecast.supp_code = input_supp_code
        forecast.price = input_price
        forecast.vol = input_vol

        db.input_data(forecast= forecast)

        st.success('Previsão cadastrada com sucesso')