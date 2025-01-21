🎵 Billboard Time Traveler 🎶
Create personalized Spotify playlists based on the Billboard Hot 100 from any week in history!

📜 Description
The Billboard Time Traveler script allows you to relive the iconic hits of any week in history by creating a Spotify playlist based on the Billboard Hot 100 chart. Simply input a date, and this script will generate a playlist with the top songs from that week directly in your Spotify account!

🚀 Features
Travel Back in Time: Retrieve the Billboard Hot 100 chart for any specific date.
Spotify Playlist Creation: Automatically creates a private playlist on your Spotify account with the top songs from the selected week.
Web Scraping and Spotify Integration: Uses requests, BeautifulSoup, and spotipy to fetch chart data and interact with Spotify.
🔧 Setup & Installation
Prerequisites
Python 3.x
Spotify Developer Account (for API access)
.env file for storing sensitive credentials
Installation
Clone the repository:

bash
git clone https://github.com/prakirtibista/billboard-time-traveler.git
cd billboard-time-traveler

Install the required libraries:

bash

pip install requests beautifulsoup4 spotipy python-dotenv
Create a .env file and add the following variables:

env

URL=https://www.billboard.com/charts/hot-100
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URL=http://localhost:8888/callback

Run the script:

bash

python main.py


📅 Usage
Run the script and input a date in the format YYYY-MM-DD when prompted (e.g., 1999-08-15).
The script will fetch the Billboard Hot 100 songs from that week and create a private playlist in your Spotify account with those tracks.

🔑 Example
Input Date: 1998-12-05
Playlist Name: 1998-12-05 Top 100
Sample Tracks:
"I Don't Want to Miss a Thing" by Aerosmith
"My Heart Will Go On" by Celine Dion
"Ray of Light" by Madonna

⚠️ Notes
Songs that are not available on Spotify will be skipped with a message.
Ensure you have a valid Spotify Developer Account and fill in the .env file correctly with your credentials.
A Spotify Premium account may be required to fully utilize playlist features.

🎶 Relive the Best Music Moments from the Past. Start Creating Your Playlist Now! 🎧
