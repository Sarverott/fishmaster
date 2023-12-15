import requests
from dotenv import load_dotenv
import sys
import os

load_dotenv()
TOKEN_LINK = os.getenv('DISCORD_TOKEN')

print("### DISCORD WEBHOOK DELETE ###")

if TOKEN_LINK is None:
    if len(sys.argv)>1:
        TOKEN_LINK = sys.argv[1]
    else:
        TOKEN_LINK = input(" discord token link = ")


print(
    requests.delete(
        TOKEN_LINK
    )
)
