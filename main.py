# Standard
import os
import argparse

# Pip
# None

# Custom
from utils.get_mp3 import download_audio
from utils.get_website import local_source
from utils.add_mp3_metadata import add_metadata

# Args
#download_audio(album, local_source())
if __name__ == "__main__":

    album = "Colère"
    artist = "Podcast Français Facile"
    genre = "Dialogues"

    for root, dirs, files in os.walk("download_results"):
        for row in dirs:
            add_metadata(album = row , artist = artist, genre = genre)
