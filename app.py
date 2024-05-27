import streamlit as st
import paginas.home as home
import paginas.create as create
import paginas.list as list
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title= 'Purchase Challenge', 
    page_icon= 'icons/gm_icon.png',
    initial_sidebar_state = 'expanded'
)

pages = {'Incluir Previsão': create}

with st.sidebar:

    st.sidebar.image('icons/gm_icon.png')

    st.divider()

    page = option_menu(
        menu_title = 'Menu',
        options = ['Home', 'Incluir Previsões', 'Consultar Previsões'],
        icons= ['house-fill','database-fill-add','search'],
        menu_icon = 'cast',
        default_index =  0
    )

if page == 'Home':
    home.run()
if page == 'Incluir Previsões':
    create.run()
if page == 'Consultar Previsões':
    list.run()