from flask import Flask, jsonify, redirect, session, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import mvg_api
from spotify import get_spotify_playlists
from weather import get_weather_data
from mvg import get_mvg_departures

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

SPOTIPY_CLIENT_ID = '365aabe4528d453f955be4cbb554e5f3'
SPOTIPY_CLIENT_SECRET = '516416b5dc6c44748ed9d4ad94fe248d'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback/'

sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI, scope="user-library-read playlist-read-private")

@app.route('/')
def index():
    if 'token_info' in session:
        # Fetch data from all services
        playlists = get_spotify_playlists(session['token_info']['access_token'])
        weather = get_weather_data('Munich')
        mvg_departures = get_mvg_departures('Fraunhoferstraße')

        return jsonify({
            'spotify_playlists': playlists,
            'weather': weather,
            'mvg_departures': mvg_departures
        })
    else:
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

@app.route('/callback/')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    # Store token information in session
    session['token_info'] = token_info
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
