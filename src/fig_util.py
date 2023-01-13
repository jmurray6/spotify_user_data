import matplotlib.pyplot as plt
import os


def get_track_fig(tracks_df):
    fig, ax = plt.subplots(3, 3, figsize=(20, 20))
    x = 0
    y = 0

    for col_name in [
        'danceability',
        'energy',
        'loudness',
        'speechiness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'valence',
        'tempo'
    ]:
        data = tracks_df[col_name]
        ax[x, y].hist(data, bins=20, edgecolor='gray')
        ax[x, y].set_title(col_name.title())
        if y < 2:
            y += 1
        else:
            x += 1
            y = 0
        if x > 2:
            break
    fig.savefig(os.environ.get('FIG_OUTPUT_PATH'))
