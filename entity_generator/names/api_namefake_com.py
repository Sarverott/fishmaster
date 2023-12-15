
import requests
import json

def generateUsername():
    response=requests.get("https://api.namefake.com/")
    return json.loads(response.content)["name"]
