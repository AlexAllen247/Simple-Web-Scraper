import requests
from bs4 import BeautifulSoup

# URL of the YouTube Shorts page
url = "https://www.youtube.com/@AlexAllen247/shorts"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "lxml")

# Find elements with id="video-title"
video_titles = soup.find_all(id="video-title")

# Print the text of each video title
for title in video_titles:
    print(title.text)
