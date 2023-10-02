# DCBadges

This super simple Python script downloads game covers from [MobyGames](https://www.mobygames.com/) and saves them to a folder named `badges`. It resizes them with Pillow to 128x128 by default.

## How to use

First, create a [MobyGames](https://www.mobygames.com/) account and go to your profile. Click on API as seen in the image below.

![Profile](https://media.discordapp.net/attachments/571743491709730826/1158548521952223363/Screenshot_2023-10-02_16-36-20.png)

Copy the API key to your clipboard and make a new file named `.env` in the DCBadges directory. In that file put `API_KEY=` and then your API key.

Type `pip install -r requirements.txt` to install the required packages and then run `main.py` It should be noted that `platforms.json` is not used by the script. 