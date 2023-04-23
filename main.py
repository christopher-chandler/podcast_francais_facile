# Standard
# None

# Pip
import requests
from bs4 import BeautifulSoup

# Custom
from utils.get_mp3 import get_audio

# URL of the webpage to scrape
website = (
    "https://www.podcastfrancaisfacile.com/apprendre-le-francais/phonetique-en-francais"
)

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
