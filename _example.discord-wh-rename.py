import requests
from dotenv import load_dotenv
import sys
import os

load_dotenv()
TOKEN_LINK = os.getenv('DISCORD_TOKEN')
RENAME_CONTENT = os.getenv('DISCORD_RENAME_WEBHOOK')

print("### DISCORD WEBHOOK RENAME ###")

if TOKEN_LINK is None:
    if len(sys.argv)>1:
        TOKEN_LINK = sys.argv[1]
    else:
        TOKEN_LINK = input(" discord token link = ")

if RENAME_CONTENT is None:
    if len(sys.argv)>2:
        RENAME_CONTENT = sys.argv[2]
    else:
        RENAME_CONTENT = input(" new webhook name = ")


print(
    requests.patch(
        TOKEN_LINK,
        json={
            "name":RENAME_CONTENT,
            "channel_id":TOKEN_LINK.split("/")[-2]
        }
    )
)
