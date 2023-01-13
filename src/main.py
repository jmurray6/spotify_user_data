from spotipy_util import get_spotipy_auth, get_top_tracks
from dotenv import load_dotenv
from df_util import get_tracks_df
from fig_util import get_track_fig


def main():
    load_dotenv()
    sp = get_spotipy_auth()
    top_tracks = get_top_tracks(sp)
    tracks_df = get_tracks_df(top_tracks, sp)
    get_track_fig(tracks_df)


if __name__ == '__main__':
    main()
