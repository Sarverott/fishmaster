import requests
from dotenv import load_dotenv
import time
import sys
import os

load_dotenv()
TOKEN_LINK = os.getenv('DISCORD_TOKEN')
USERNAME = os.getenv('DISCORD_USERNAME')
AVATAR = os.getenv('DISCORD_AVATAR')
MESSAGE = os.getenv('DISCORD_MESSAGE')

print("### DISCORD WEBHOOK SEND MESSAGE ###")

if TOKEN_LINK is None:
    if len(sys.argv)>1:
        TOKEN_LINK = sys.argv[1]
    else:
        TOKEN_LINK = input(" discord token link = ")

if USERNAME is None:
    if len(sys.argv)>3:
        USERNAME = int(sys.argv[3])
    else:
        USERNAME = input(" USERNAME = ")

if AVATAR is None:
    if len(sys.argv)>4:
        AVATAR = int(sys.argv[4])
    else:
        AVATAR = input(" AVATAR URL = ")

if MESSAGE is None:
    if len(sys.argv)>2:
        MESSAGE = int(sys.argv[2])
    else:
        MESSAGE = input(" MESSAGE = ")

print(
    requests.post(
        TOKEN_LINK,
        json={
            'avatar_url':AVATAR,
            'username':USERNAME ,
            'content':MESSAGE
        }
    )
)
