import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("REDACTED", 
    "REDACTED"
auth.set_access_token("REDACTED"
    "REDACTED")# 
# bearer token: REDACTED 

def test_auth():
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


api = tweepy.API(auth, wait_on_rate_limit=True)

def create_blocks(s):
    t = s.split(" ")
    
    charcount = 0
    curr_word = 0

    curr_block = ""
    blocks = []
    block_count = 1
    charlim = 273
    
    while curr_word < len(t):
        while curr_word < len(t) and len(curr_block) + len(t[curr_word]) < charlim:
            curr_block += t[curr_word] + " "
            curr_word += 1
        blocks.append(curr_block)
        block_count += 1
        curr_block = ""

    blocks = [blocks[0] + "..."] + ["..." + block + "..." for block in blocks[1:-1]] + ["..." + blocks[-1]]
    assert all(len(block) < 280 for block in blocks)
    return blocks

def post_story(s):
    s_blocks = create_blocks(s)
    last_tweet = api.update_status(status=s_blocks[0])
    for i in range(1,len(s_blocks)):
        last_tweet = api.update_status(status=s_blocks[i], 
                                 in_reply_to_status_id=last_tweet.id, 
                                 auto_populate_reply_metadata=True)

# import sys
# n = int(sys.argv[1])
import random
n = random.randint(103,2342)
assert 103 <= n and n <= 2342
f = open("/home/private/goodstorybot/stories/s" + str(n) + ".txt", 'r')
s = str(n) + ". " + "".join(f.readlines()) + "THE END."
post_story(s)

from datetime import datetime
datetime.now()
print(datetime.now(), end=": ")
print("Successfully tweeted story " + str(n) + ".")
