import streamlit as st
import paginas.home as home
import paginas.create as create
import paginas.list as list
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


st.set_page_config(
    page_title='Purchase Challenge',
    page_icon='icons/gm_icon.png',
    layout = 'wide'
)

with open('config.yaml') as file:
    config = yaml.load(file, Loader = SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login()

if st.session_state['authentication_status']:

    pages = {'Incluir Previsão': create}
    
    with st.sidebar:
        authenticator.logout()
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
        create.run(st.session_state.username)
    if page == 'Consultar Previsões':
        list.run()

elif st.session_state['authentication_status'] is False:
    st.error('Usuário/Senha inválido')

elif st.session_state['authentication_status'] is None:
    st.warning('Insira suas credenciais')