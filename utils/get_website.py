# Standard
# None

# Pip
import requests
from bs4 import BeautifulSoup

# Custom

from .get_mp3 import get_audio

def internet_source(website):

    # Send a GET request to the URL and get the HTML content
    response = requests.get(website)
    html_content = response.content

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find elements using tags, classes, or IDs

    website_links = soup.find_all("a", href=True)
    data = list()

    for link in website_links:
        href = link["href"]
        try:
            get_audio(href)
        except Exception as e:
            pass


def local_source():
    # Parse the HTML content using Beautiful Soup
    html_content = open("local_html_files/incoming.html", mode="r").read()
    soup = BeautifulSoup(html_content, "html.parser")

    # Find elements using tags, classes, or IDs
    website_links = soup.find_all("a", href=True)
    results = dict()

    for row in website_links:
        results[row.getText()]=row["href"]

    return results