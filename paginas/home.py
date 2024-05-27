import streamlit as st

def run():
    

    st.header(':shopping_trolley: Purchasing Challenge')
    st.subheader(':pencil2: Danilo Jang')
    st.divider()

    st.markdown(
    '''
        Esta solução foi desenvolvida com o objetivo de atender o desafio de criar uma ferramenta na qual os analistas possam inserir dados de previsão de faturamento dos fornecedores nos próximos anos.
    '''
    )

    st.markdown(
    '''
    Esta aplicação consiste em duas páginas:

    - Página de Inclusão de Previsões: Aqui, os usuários podem inserir os dados de previsão. Ao clicar no botão 'Cadastrar', esses dados são armazenados no banco de dados.

    - Página de Consulta de Previsões: Nesta página, os usuários têm acesso a todos os dados de previsão inseridos, podendo aplicar filtros conforme necessário.
    '''
    )
