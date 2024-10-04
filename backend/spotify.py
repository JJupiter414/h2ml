import spotipy

def get_spotify_playlists(access_token):
    sp = spotipy.Spotify(auth=access_token)
    playlists = sp.current_user_playlists()
    return [{'name': playlist['name'], 'total_tracks': playlist['tracks']['total']} for playlist in playlists['items']]
