
from bs4 import BeautifulSoup
import requests

def generateMessage():
    randomMessageWebpage=requests.get("https://randomword.com/sentence")
    infosoup=BeautifulSoup(randomMessageWebpage.content, 'html.parser')
    return infosoup.find(id="random_word").string
