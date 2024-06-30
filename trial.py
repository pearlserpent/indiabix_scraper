import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36",
}

url = "https://www.indiabix.com/aptitude/problems-on-trains/"

response = requests.get(url, headers=headers, verify=False)

soup = BeautifulSoup(response.text, "html.parser")

div = soup.findAll("div", {"class": "bix-div-container"})

questions = div.findAll("div", {"class": "bix-td-qtxt table-responsive w-100"})

print(type(div))
