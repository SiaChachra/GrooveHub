# spotify_client.py

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from lastfm_client import LastFMClient  # Ensure this file is in the same directory

# Spotify API credentials
SPOTIFY_CLIENT_ID = '613054455d134585a26c8c1ea0f3f171'
SPOTIFY_CLIENT_SECRET = '312e93ce7dcf4bd7a14d501ee2fa8fc3'

class SpotifyClient:
    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID, 
            client_secret=SPOTIFY_CLIENT_SECRET
        )
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def search_artist(self, artist_name):
        """Search for an artist and return artist details."""
        results = self.spotify.search(q=artist_name, type='artist', limit=1)
        return results['artists']['items'][0] if results['artists']['items'] else None

    def get_top_tracks(self, artist_id):
        """Fetch top 5 tracks of the artist."""
        results = self.spotify.artist_top_tracks(artist_id)
        return [track['name'] for track in results['tracks'][:5]]

    def get_albums(self, artist_id):
        """Fetch top 5 albums of the artist."""
        results = self.spotify.artist_albums(artist_id, album_type='album')
        album_names = []
        unique_albums = set()  # To avoid duplicate albums
        for album in results['items']:
            if album['name'] not in unique_albums:
                album_names.append(album['name'])
                unique_albums.add(album['name'])
            if len(album_names) == 5:
                break
        return album_names

# Main function to get user input and display artist info
def main():
    spotify_client = SpotifyClient()
    lastfm_client = LastFMClient()
    
    # Get artist name from user input
    artist_name = input("Enter the name of the artist: ")
    artist_info = spotify_client.search_artist(artist_name)
    
    if artist_info:
        print(f"\nArtist: {artist_info['name']}")
        
        # Get and display top hits
        top_tracks = spotify_client.get_top_tracks(artist_info['id'])
        print("\nTop Hits:")
        for i, track in enumerate(top_tracks, 1):
            print(f"{i}. {track}")
        
        # Get and display top albums
        top_albums = spotify_client.get_albums(artist_info['id'])
        print("\nTop Albums:")
        for i, album in enumerate(top_albums, 1):
            print(f"{i}. {album}")
        
        # Get and display biography
        bio = lastfm_client.get_artist_bio(artist_name)
        print("\nBiography:")
        print(bio)
    else:
        print("Artist not found.")

if __name__ == "__main__":
    main()
