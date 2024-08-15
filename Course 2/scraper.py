import requests
import random
from bs4 import BeautifulSoup 
from colorama import Fore

url="https://pixelford.com/blog"
number=random.randint(10000000,999999999999)
response=requests.get(url, headers={"user-agent": f"{number}"})
html = response.content

soup = BeautifulSoup(html, "html.parser")

print(soup)

a_tags = soup.find_all("a", class_="entry-title-link")

print(number)

for a_tag in a_tags:
    print(Fore.GREEN+f"{a_tag.get_text()}")