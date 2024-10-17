"""
Doc String
"""
from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum ator encontrado.')

    st.title('Cadastrar novo Ator')
    name = st.text_input('Nome do Ator:')
    birthday = st.date_input(
        label='Data de Lançamento:',
        min_value=datetime(1800, 1, 1).date(),
        format='DD/MM/YYYY',
    )
    nationality = st.selectbox(
        label='Nacionalidade:',
        options=['USA', 'BRAZIL', 'UK'],
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar Ator. Verifique os campos.')
