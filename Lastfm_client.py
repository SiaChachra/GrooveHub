# lastfm_client.py

import requests

# Last.fm API credentials
LAST_FM_API_KEY = 'your_last_fm_api_key'

class LastFMClient:
    def __init__(self):
        self.api_key = LAST_FM_API_KEY

    def get_artist_bio(self, artist_name):
        """Fetch artist biography from Last.fm."""
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={self.api_key}&format=json"
        response = requests.get(url)

        # Debugging: Print the full response to check for errors
        print("API Response:", response.status_code, response.json())

        if response.status_code == 200:
            data = response.json()
            # Check if 'bio' exists in the data structure
            if 'artist' in data and 'bio' in data['artist']:
                bio = data['artist']['bio']['summary']
                return bio
            else:
                return "Biography not available for this artist."
        else:
            return "Failed to fetch artist biography due to an API error."

# Example usage
if __name__ == "__main__":
    lastfm_client = LastFMClient()
    artist_name = input("Enter the artist's name: ")
    
    # Fetch and print artist biography
    bio = lastfm_client.get_artist_bio(artist_name)
    print(f"\nBiography:\n{bio}")
