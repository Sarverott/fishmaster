
import string
import random

def generateAvatarUrl():
    cacheBlinder=''.join(random.choice(string.ascii_lowercase) for i in range(20))
    return 'https://thispersondoesnotexist.com/?this_is_discord_cache_blinder='+cacheBlinder
