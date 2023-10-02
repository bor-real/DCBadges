import io
import os
import time
import json
import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Constants
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.mobygames.com/v1/"
PLATFORM_ID = 8
LIMIT = 40
RESIZE_DIMENSIONS = (128, 128)
FOLDER_NAME = "badges"

# Function to download covers
def download_covers():
    # Create folder if it doesn't exist
    if not os.path.exists(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)

    # Fetch a list of games for the specified platform
    games_url = f"{BASE_URL}games?platform={PLATFORM_ID}&limit={LIMIT}&format=id&api_key={API_KEY}"
    game_list_response = requests.get(games_url)
    game_list_data = json.loads(game_list_response.text)
    
    # Iterate through the games and download their covers
    for game_id in game_list_data["games"]:
        time.sleep(1)  # For rate limiting reasons

        # Fetch cover information for the game
        covers_url = f"{BASE_URL}games/{game_id}/platforms/{PLATFORM_ID}/covers?api_key={API_KEY}"
        covers_response = requests.get(covers_url)
        covers_data = json.loads(covers_response.text)

        try:
            # Get the URL of the cover image
            # This just uses the first image it can. I don't care that it mixes and matches regions. 

            cover_image_link = covers_data['cover_groups'][0]['covers'][0]['image'] 
            
            # Download and resize the cover image
            cover_image = Image.open(io.BytesIO(requests.get(cover_image_link).content))
            print(f"Downloading cover for {game_id}.")
            cover_image.resize(RESIZE_DIMENSIONS).save(os.path.join(FOLDER_NAME, str(game_id) + ".png"))

        except IndexError:
            print(f"{game_id} doesn't have any covers.")

    print("Downloading complete.")

# Main function
if __name__ == "__main__":
    download_covers()
