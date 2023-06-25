# Standard
import csv
import glob
import os
import re
import shutil

# Pip
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC


# Custom
# None

def add_metadata(**kwargs) -> None:
    artist = kwargs.get("artist")
    album = kwargs.get("album")
    genre = kwargs.get("genre")


    mp3_files = glob.glob(f"/Users/christopherchandler/Github"
                          f"/Python/podcast_francais_facile/"
                          f"download_results/{album}/*.mp3")

    for mp3_audio in sorted(mp3_files):
        try:
            mp3_name = re.search(r"\/([\w\s.*’&-]+\.mp3)",
                                 mp3_audio).group(1).replace(".mp3","")

        except:
            mp3_name = mp3_audio.split("/")[-1]
        # Set audio
        audio = EasyID3(mp3_audio)

        # Set Metadata
        audio["artist"] = artist
        audio["album"] = album
        audio["title"] = mp3_name
        audio["genre"] = genre
 
        print(mp3_name)
        # Save metadata
        audio.save()
    print("Metadata has been added.")
