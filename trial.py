import requests
from PIL import Image
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

#
#print(question)

## As the explanation contains iamges and gifs for brackets and other symbols
## it is hard to parse and save the text from it
## So the best option is to currently save the explanation in the html format
## and store the symbols in a folder in the similar directory as of the website
## for example - <td class="ga-td-line" rowspan="2"><img src="/_files/images/aptitude/1-sym-oparen-h1.gif"/></td>

explanation = div.find("div", {"class": "bix-ans-description table-responsive"})
#explanation = div.find("table", {"class": "ga-tbl-answer"})
print(explanation)
