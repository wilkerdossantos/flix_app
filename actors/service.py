import streamlit as st
from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        del st.session_state.actors
        return self.actor_repository.create_actor(actor)
