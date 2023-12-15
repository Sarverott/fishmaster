import requests
from dotenv import load_dotenv
import time
import sys
import os

from entity_generator import avatar
from entity_generator import messages
from entity_generator import names
from entity_generator import pictures

load_dotenv()
TOKEN_LINK = os.getenv('DISCORD_TOKEN')
SPAM_COUNT = os.getenv('DISCORD_SPAM_COUNT')

print("### DISCORD WEBHOOK SEND RANDOM SPAM MESSAGES ###")

if TOKEN_LINK is None:
    if len(sys.argv)>1:
        TOKEN_LINK = sys.argv[1]
    else:
        TOKEN_LINK = input(" discord token link = ")

if SPAM_COUNT is None:
    if len(sys.argv)>2:
        SPAM_COUNT = int(sys.argv[2])
    else:
        SPAM_COUNT = 255

for i in range(SPAM_COUNT):

    time.sleep(1)

    avatar_url=avatar.useM("thispersondoesnotexist.com")
    username=names.useM("api.namefake.com")
    content=messages.useM("randomword.com")

    print()

    print("  ### Message ", i, " ####")
    print("avatar_url: ", avatar_url)
    print("username: ", username)
    print("content: ", content)
    print()

    print(
        requests.post(
            TOKEN_LINK,
            json={
                'avatar_url':avatar_url,
                'username':username ,
                'content':content
            }
        )
    )
