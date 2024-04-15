from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Set up WebDriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL of the YouTube Shorts page
url = "https://www.youtube.com/@AlexAllen247/shorts"
driver.get(url)

# Wait for JavaScript to load
time.sleep(5)

# Extract titles
titles = [element.text for element in driver.find_elements_by_css_selector('h3.title')]  # Adjust selector as needed

# Print the titles
print(titles)

# Clean up
driver.quit()
