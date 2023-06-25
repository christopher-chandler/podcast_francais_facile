# Standard
import os
import re

# Pip
import requests

from bs4 import BeautifulSoup

# Custom
# None

results_folder = f"download_results"

def get_audio(sub_folder,name, url) -> None:

    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, "html.parser")
    bs4_scrape = soup.findAll("audio", class_="wp-audio-shortcode")

    i = 0
    os.makedirs(f"{results_folder}/{sub_folder}", exist_ok=True)
    for mp3 in bs4_scrape:
        mp3_url = mp3.source["src"]

        # Send a GET request to the mp3 URL and get the content
        response = requests.get(mp3_url)
        mp3_content = response.content

        # Save the content to a local file
        name = name.replace("/",("_"))
        save_location = f"{results_folder}/{sub_folder}/{name}_{i}.mp3"
        with open(save_location, "wb") as f:
            f.write(mp3_content)
        i += 1

def download_audio(sub_folder,website_links) -> None:
    i = 0
    for link in website_links:
        try:
            i+=1
            prog = round(i / len(website_links),2)
            print(prog)
            get_audio(sub_folder,link,website_links.get(link))
        except Exception as e:
            print(e)

    return None

if __name__ == "__main__":
    pass
