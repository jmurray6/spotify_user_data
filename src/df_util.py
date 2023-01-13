import pandas as pd


def get_artists(x):
    artists = []
    for block in x:
        artists.append(block.get('name'))
    return artists


def get_tracks_df(top_tracks, sp):
    tracks_df = pd.json_normalize(top_tracks.get('items'))
    tracks_df['artist_names'] = tracks_df.artists.apply(
        lambda x: get_artists(x)
    )
    for col in tracks_df.columns:
        if col not in ['name', 'id', 'artist_names']:
            del tracks_df[col]
    tracks_df = tracks_df.set_index('id')
    af_df = pd.DataFrame(sp.audio_features(tracks_df.index))
    rich_df = tracks_df.merge(af_df, how='left', on='id')
    for col in ['type', 'uri', 'track_href', 'duration_ms', 'analysis_url']:
        del rich_df[col]
    return rich_df
