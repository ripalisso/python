import spotipy
from spotipy.oauth2 import SpotifyOAuth

# aqui é pra colocar suas informações do seu app criado lá no spotify developers dashboard
SPOTIPY_CLIENT_ID = 'coloque seu id de client aqui'
SPOTIPY_CLIENT_SECRET = 'coloque seu client secret aqui'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'

# configura a permissão do bagui
SCOPE = "playlist-read-private"

# cria a instância do client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

# pega o link
playlist_uri = input("Insira o link da playlist (Spotify): ")

# pega as informações
playlist_info = sp.playlist_tracks(playlist_uri)

# percore e imprime as informações
for track in playlist_info['items']:
    track_name = track['track']['name']
    track_artists = ", ".join([artist['name'] for artist in track['track']['artists']])
    print(f"Nome da música: {track_name}")
    print(f"Artista(s): {track_artists}")
    print("\n")

