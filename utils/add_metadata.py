# Standard
import csv
import glob
import os
import re
import shutil

# Pip
from mutagen.easyid3 import EasyID3

os.chdir("/Users/christopherchandler/Github/Python/PodcastFrancaisFacile/results")

res = open(
    "/Users/christopherchandler/Github/Python/PodcastFrancaisFacile/csv_results/anki_2.csv",
    mode="w",
    encoding="utf-8",
)
csv_writer = csv.writer(res)


for f in os.listdir(os.getcwd()):
    mp3 = glob.glob(f"{f}/*.mp3")

    for mp3_audio in sorted(mp3):

        mp3_name = re.search(r"\/([\w-]+\.mp3)", mp3_audio).group(1).replace(".mp3", "")
        n = f"[sound:{mp3_name}.mp3]"
        print(n, f)
        csv_writer.writerow([mp3_name, n,mp3_name, f,f])

        file = f"{f}/{mp3_audio}"
        audio = EasyID3(mp3_audio)

        dst = f"/Users/christopherchandler/Library/Application Support/Anki2/Main Anki/collection.media/{mp3_name}.mp3"
        shutil.copy(mp3_audio, dst)

        audio["artist"] = "Podcast Français Facile"
        audio["album"] = f
        audio["title"] = mp3_name
        audio["genre"] = "Pronunciation"

        audio.save()
    print("#" * 10)
