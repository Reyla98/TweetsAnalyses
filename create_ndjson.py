# -*- coding: utf-8 -*-

"""
Created on Thu Feb 20 17:37:22 2020

@author: Laurnae Castiaux
"""

import tweepy
import twitterscraper as ts
import json
from twitter_authentication import myAuthentication
import re
from pprint import pprint

api = myAuthentication() #authenticates the program on my dev Twitter account

def tweepySearch():
    with open("Alost.ndjson", 'a') as output:

        for pages in tweepy.Cursor(api.search,
                                    q='#OilsjtCarnaval',
                                    tweet_mode = 'extended',
                                    #lang='fr',
                                    include_entities = True,
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


def getLang(Text):
    keepLang = re.compile("lang=\"(..)\"")
    Lang = re.search(keepLang, Text)
    try:
        return Lang.group(1)
    except:
        return ""


def remove_html_tags(text):
    # First , we keep the emojis
    keep_emojis = re.compile('<img alt=\"(.+?)\" aria-label=\"Emoji.+?>')
    # After that , we remove all the HTML tags ( between < and >)
    clean_html_tags = re.compile('<.+?>')
    # Applying the ’keep_emojis ’ regex
    tweet_with_emojis = re.sub(keep_emojis, '\\1', text)
    # Applying the ’clean_html_tags ’ regex
    return re.sub(clean_html_tags, '', tweet_with_emojis)


def twitterscraperSearch():
    with open("Alost_user.ndjson", "a", newline='') as output:
        list_of_tweets = ts.query_tweets("Aalst (from:HLN_BE) until:2020-03-01 since:2020-02-14", 30)
        for tweet in list_of_tweets:
            json_data = json.dumps({"tweet_id": int(tweet.tweet_id),
                                    "screen_name":tweet.screen_name,
                                    "user_id": int(tweet.user_id),
                                    "created_at":str(tweet.timestamp), #sinon, format date, mais pas reconnu par json
                                    "entities.hashtags":[{"text":x} for x in tweet.hashtags],
                                    "entities.user_mentions":[],
                                    "lang":getLang(tweet.text_html),
                                    "full_text": remove_html_tags(tweet.text_html)})
            output.writelines(json_data+"\n")


if __name__ == '__main__':
    twitterscraperSearch()