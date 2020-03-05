# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:37:22 2020

@author: Laurnae Castiaux
"""

import tweepy
import json
from authentication import authentication

api = authentication() #authenticates the program on my dev Twitter account

with open("test.ndjson", 'a') as output:

    for pages in tweepy.Cursor(api.search,
                                q='lovely',       #Queries made on "Oilsjt carnaval", "carnalval Alost", aalst carnaval
                                tweet_mode = 'extended',
                                #lang='fr',
                                include_entities = True,
                                include_rts = False,
                                ).pages():

            for tweet in pages:
                print(str(tweet.id)+" - "+str(tweet.created_at))
                json_data = json.dumps({"tweet_id": tweet.id,
                                        "screen_name":tweet.user.screen_name,
                                        "user_id": tweet.user.id,
                                        "created_at":str(tweet.created_at), #sinon, format date, mais pas reconnu par json
                                        "entities.hashtags":tweet.entities['hashtags'],
                                        "entities.user_mentions":tweet.entities['user_mentions'],
                                        "lang":tweet.lang,
                                        "full_text": tweet.full_text})
                output.writelines(json_data+"\n")
    
