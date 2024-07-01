import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36",
}

url = "https://www.indiabix.com/aptitude/problems-on-trains/"

response = requests.get(url, headers=headers, verify=False)

soup = BeautifulSoup(response.text, "html.parser")

divs = soup.findAll("div", {"class": "bix-div-container"})

div = divs[0]

question = div.find("div", {"class": "bix-td-qtxt table-responsive w-100"})
options = div.findAll("div", {"class": "flex-wrap"})
answer = div.find("input", {"class": "jq-hdnakq"})


""" if question:
    # Do something with the question
    print(question.text)
    for option in options:
        print(option.text)
        

print("Answer: ", answer.get("value")) """

#explanation = div.find("div", {"class": "bix-ans-description table-responsive"})
explanation = div.find("table", {"class": "ga-tbl-answer"})
print(explanation.text)
