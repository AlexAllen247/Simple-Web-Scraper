import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = ""
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "lxml")

# Extract the CSS code
css_links = []
for link in soup.find_all("link", {"rel": "stylesheet"}):
    css_url = link["href"]
    if not css_url.startswith(("http://", "https://")):
        css_url = urljoin(url, css_url)
    css_links.append(css_url)

css_code = ""
for link in css_links:
    css_response = requests.get(link)
    css_code += css_response.text

# Extract the HTML code
html_code = soup.prettify()

# Save the CSS and HTML code to files
with open("styles.css", "w") as file:
    file.write(css_code)

with open("index.html", "w") as file:
    file.write(html_code)
