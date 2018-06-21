import spotipy

katyperry_uri = 'spotify:artist:6jJ0s89eD6GaHleKKya26X'

spotify = spotipy.Spotify()

results = spotify.artist_albums(katyperry_uri, album_type = 'album')

albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print((album['name']))