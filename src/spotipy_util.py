import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def get_spotipy_auth():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
            client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
            redirect_uri=os.environ.get('SPOTIPY_REDIRECT_URI'),
            scope=os.environ.get('SCOPE')
        )
    )
    return sp


def get_top_tracks(sp):
    return sp.current_user_top_tracks(
        limit=os.environ.get('NUMBER_OF_SONGS'),
        offset=0,
        time_range=os.environ.get('TIME_RANGE')
    )
