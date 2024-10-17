import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de Filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero',
        )
        st.plotly_chart(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        color_col1 = '#795014'
        total_movies_card = create_cards(
            'Total de Filmes Cadastrados',
            movie_stats['total_movies'],
            color_col1,
        )
        st.plotly_chart(total_movies_card)

    with col2:
        color_col2 = '#191970'
        total_reviews_card = create_cards(
            'Total de Avaliações Cadastradas',
            movie_stats['total_reviews'],
            color_col2,
        )
        st.plotly_chart(total_reviews_card)

    with col3:
        color_col3 = '#800000'
        average_stars_card = create_cards(
            'Média Geral de Estrelas nas Avaliações',
            movie_stats['average_stars'],
            color_col3,
        )
        st.plotly_chart(average_stars_card)

    st.subheader('Filmes por Gênero')
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")


def create_cards(title, value, color):
    fig = go.Figure(go.Indicator(
        mode="number",
        value=value,
        title={'text': title, 'font': {'size': 13}},
        number={'font': {'size': 50}}
    ))
    fig.update_layout(
        paper_bgcolor=color,
        height=200
    )
    return fig
