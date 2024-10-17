"""
Doc String
"""
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            reviews_df,
            key='review_grid',
        )
    else:
        st.warning('Nenhuma Review encontrada.')

    st.title('Cadastrar nova review')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movies_titles = {movie['title']: movie['id'] for movie in movies}
    movie = st.selectbox(
        label='Filme:',
        options=list(movies_titles.keys()),
    )

    stars_mapping = [star for star in range(1, 6)]
    st.write('Estrelas:')
    stars = st.feedback('stars')
    comment = st.text_area('Comentário:')

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movies_titles[movie],
            stars=stars_mapping[stars],
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar Review. Verifique os campos.')
