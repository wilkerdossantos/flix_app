import requests
import streamlit as st
from login.service import logout


class MovieRepository:

    def __init__(self):
        self.__base_url = 'https://flixapi.umbytedeideias.com.br/api/v1/'
        self.__movie_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movie_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movie_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        print(response.json())
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movie_url}stats/',
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
