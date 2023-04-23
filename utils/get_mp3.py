# Standard
import csv
import os

# Pip
import requests
import re

from bs4 import BeautifulSoup

save_file_anki = open(
    r"/Users/christopherchandler/Github/Python/PodcastFrancaisFacile/csv_results/anki.csv",
    mode="a",
    encoding="utf-8",
)
csv_writer = csv.writer(save_file_anki)
l = list()


def get_audio(url) -> None:

    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, "html.parser")

    # Create the folder
    folder_name = re.search(r"\/([\w-]+\.html)", url).group(1)
    folder_name = folder_name.replace(".html", "").replace("-", "_")

    results_folder = f"results/{folder_name}"
    os.makedirs(results_folder, exist_ok=True)

    bs4_scrape = soup.findAll("audio", class_="wp-audio-shortcode")
    audio_text_one = soup.findAll("ol")
    audio_text_two = soup.findAll(
        "div", class_="panel-body toggle-content fusion-clearfix"
    )
    i = 0

    print(folder_name)
    print(len(audio_text_one))
    print(audio_text_two)
    for mp3 in bs4_scrape:
        mp3_text_one = audio_text_one[i]
        mp3_text_two = audio_text_two[i]

        mp3_name = re.search(r"\/([\w-]+\.mp3)", mp3.source["src"]).group(1)
        mp3_url = mp3.source["src"]

        # Send a GET request to the mp3 URL and get the content
        response = requests.get(mp3_url)
        mp3_content = response.content

        # Save the content to a local file
        save_location = f"{results_folder}/{mp3_name}"


        if mp3_text_one:
            mp3_name_audio = f"[sound:{mp3_name}]"
            info = [mp3_text_one, mp3_name_audio, folder_name]
            csv_writer.writerow(info)

        elif mp3_text_two:
            mp3_name_audio = f"[sound:{mp3_name}]"
            info = [mp3_text_two, mp3_name_audio, folder_name]
            csv_writer.writerow(info)


        with open(save_location, "wb") as f:
            f.write(mp3_content)
        i += 1


if __name__ == "__main__":
    pass
