"""
Doc String
"""
from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            movies_df,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum Filme encontrado.')

    st.title('Cadastrar novo Filme')

    title = st.text_input('Título:')

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genres_names = {genre['name']: genre['id'] for genre in genres}
    genre = st.selectbox(
        label='Gênero:',
        options=list(genres_names.keys()),
    )

    release_date = st.date_input(
        label='Data de Lançamento:',
        min_value=datetime(1800, 1, 1).date(),
        format='DD/MM/YYYY',
    )

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actors_names = {actor['name']: actor['id'] for actor in actors}
    actors_multiselect = st.multiselect(
        label='Atores:',
        options=actors_names.keys()
    )

    resume = st.text_area('Resumo:')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            genre=genres_names[genre],
            realease_date=release_date,
            actors=[actors_names[actor] for actor in actors_multiselect],
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar Filme. Verifique os campos.')
