# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:28:39 2020

@author: laura
"""

import json
import re
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

def dictMaxValues(dictionnary, n):
    """
    Return the n first elements of a dictionnary
    
    args:
    dictionnary is a dictionnary with int or float as values
    n is the number of wanted elements (n <= len(dictionnary))

    Return a list of tuples with the key and value of the n elements
    that have the biggest value.
    """

    # Create a list of tuples sorted by index 1 i.e. value field     
    listofTuples = sorted(dictionnary.items() , reverse=True, key=lambda x: x[1])
 
    # Select the n first tuples
    firstTuples = []
    for elem in listofTuples :
        if n >=0:
            firstTuples.append(elem)
            n -= 1
        else:
            break

    return firstTuples


def advancedSearch(file, tweet_id=None,
                            screen_name=None,
                            user_id=None,
                            date=None,
                            hashtags=None,
                            mentions=None,
                            lang=None,
                            contains=None):
    """
    Return a list of tweets corresponding to the search
    
    args:
    date must be in format JJJJ-MM-DD
    hashtags must be a list of the wanted hashtags (without "#")
    mentions must be a list of the wanted mentions (without "@")
    lang must be the ISO code of the language 
    contains must be a list of all the strings wanted in the text
    """

    with open(file, "r") as tweet_corpus:
        n = 0
        matched_tweets = []

        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            tweet_date = re.match("(.{4}-.{2}-.{2}) .*", tweet['created_at']).group(1)
            
            if (tweet_id is None or tweet_id == tweet["tweet_id"])\
            and (screen_name is None or screen_name == tweet["screen_name"])\
            and (user_id is None or user_id == tweet["user_id"])\
            and (date is None or date == tweet_date)\
            and (hashtags is None or all(tag in tweet["entities.hashtags"] for tag in hashtags))\
            and (mentions is None or all(mention in tweet["mentions"] for mention in menstions))\
            and (lang is None or lang == tweet["lang"])\
            and (contains is None or all(word in tweet["full_text"].split() for word in contains)):
                matched_tweets.append(tweet)

    return matched_tweets


def printTweets(tweet_list):
    """
    Print the tweet_id followed by the full_text

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)
    """

    for tweet in tweet_list:
        print("{} : {}\n".format(tweet["tweet_id"], tweet["full_text"]))


def countTags(tweet_list):
    """
    Count the frequency of each hashtag in a list containing tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with hashtags as key and their frequency as value
    """

    hashtags_count = {}
    
    for tweet in tweet_list:
        for tag in tweet["entities.hashtags"]:
            # update hashtag_count
            hashtags_count[tag["text"]] = hashtags_count.setdefault(tag["text"], 0)
            hashtags_count[tag["text"]] += 1
    return hashtags_count


def countMention(tweet_list):
    """
    Count the frequence of each mention in a list containing tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with mentions as key and their frequency as value
    """

    mention_count = {}
    mention_pattern = re.compile("@[\w]+")
    
    for tweet in tweet_list:
        mentions = re.findall(mention_pattern, tweet["full_text"])

        for mention in mentions:
            # update mention_count
            mention_count[mention] = mention_count.setdefault(mention, 0)
            mention_count[mention] += 1

    return mention_count


def countTweetsPerUser(tweet_list):
    """
    Count the number of tweets of each user in a list containing tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with user_screename as key and their frequency as value
    """

    TweetsPerUser_count = {}
    
    for tweet in tweet_list:
        user = tweet['screen_name']

        # update TweetsPerUser_count
        TweetsPerUser_count[user] = TweetsPerUser_count.setdefault(user, 0)
        TweetsPerUser_count[user] += 1

    return TweetsPerUser_count


def countTweetPerDay(tweet_list):
    """
    Count the number of tweets per day in a list containing tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with the date as key and the nuber of tweet as value
    """

    TweetsPerDay_count = {}
    
    for tweet in tweet_list:
        date = re.match("(.{4}-.{2}-.{2}) .*", tweet['created_at']).group(1)

        # update TweetsPerDay_count
        TweetsPerDay_count[date] = TweetsPerDay_count.setdefault(date, 0)
        TweetsPerDay_count[date] += 1

    return TweetsPerDay_count


def countLang(tweet_list):
    """
    Count the number of tweets in each language in a list of tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with hashtags as key and their frequency as value
    """
    lang_count = {}
        
    for tweet in tweet_list:
        lang_count["lang"] = lang_count.setdefault(tweet["lang"], 0)
        lang_count[tweet["lang"]] += 1

    return lang_count


if __name__ == '__main__':

    ES = advancedSearch("Alost_corpus.ndjson", lang="es", contains=['Puigdemont'])
    print(len(ES))
    pprint(dictMaxValues(countTags(ES), 50))