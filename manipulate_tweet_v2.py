# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:28:39 2020

@author: Laurane Castiaux
"""

import json
import re
from pprint import pprint


def dictMaxValues(dictionary, n=100):
    """
     Return list of tuples of the n elements in dictionary with the highest value
    
    args:
    dictionary is a dictionary with int or float as values
    n is the number of wanted elements (default: n=100)
    """

    # Create a list of tuples sorted by index 1 i.e. value field     
    listofTuples = sorted(dictionary.items() , reverse=True, key=lambda x: x[1])
 
    # Select the n first tuples
    firstTuples = []
    for elem in listofTuples :
        if n >= 0:
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
    contains must be a list of all the words (in lowercase) wanted in the text
    """

    with open(file, "r") as tweet_corpus:
        matched_tweets = []

        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            tweet_date = re.match("(.{4}-.{2}-.{2}) .*", tweet['created_at']).group(1)
            tweet_text = [e.lower() for e in tweet["full_text"].split()]
            tweet_tags = [tag["text"] for tag in tweet["entities.hashtags"]]
            tweet_mentions = [mention["screen_name"] for mention in tweet["entities.user_mentions"]]
            
            if (tweet_id is None or tweet_id == tweet["tweet_id"])\
            and (screen_name is None or screen_name == tweet["screen_name"])\
            and (user_id is None or user_id == tweet["user_id"])\
            and (date is None or date == tweet_date)\
            and (hashtags is None or all(tag in tweet_tags for tag in hashtags))\
            and (mentions is None or all(mention in tweet_mentions for mention in mentions))\
            and (lang is None or lang == tweet["lang"])\
            and (contains is None or all(word in tweet_text for word in contains)):
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

    Return a dictionary with hashtags as key and their frequency as value
    """

    hashtags_count = {}
    
    for tweet in tweet_list:
        for tag in tweet["entities.hashtags"]:
            # update hashtag_count
            hashtags_count[tag["text"]] = hashtags_count.setdefault(tag["text"], 0)
            hashtags_count[tag["text"]] += 1
    return hashtags_count


def countMentions(tweet_list):
    """
    Count the frequence of each mention in a list containing tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionary with mentions as key and their frequency as value
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

    Return a dictionary with user_screename as key and their frequency as value
    """

    TweetsPerUser_count = {}
    
    for tweet in tweet_list:
        user = tweet['screen_name']

        # update TweetsPerUser_count
        TweetsPerUser_count[user] = TweetsPerUser_count.setdefault(user, 0)
        TweetsPerUser_count[user] += 1

    return TweetsPerUser_count


def countTweetsPerDay(tweet_list):
    """
    Count the number of tweets per day in a list containing tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionary with the date as key and the nuber of tweet as value
    """

    TweetsPerDay_count = {}
    
    for tweet in tweet_list:
        date = re.match("(.{4}-.{2}-.{2}) .*", tweet['created_at']).group(1)

        # update TweetsPerDay_count
        TweetsPerDay_count[date] = TweetsPerDay_count.setdefault(date, 0)
        TweetsPerDay_count[date] += 1

    return TweetsPerDay_count


def countLangs(tweet_list):
    """
    Count the number of tweets in each language in a list of tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionary with language as key and their frequency as value
    """

    lang_count = {}
        
    for tweet in tweet_list:
        lang_count["lang"] = lang_count.setdefault(tweet["lang"], 0)
        lang_count[tweet["lang"]] += 1

    return lang_count


def countWords(tweet_list, stopList=None):
    """
    Count the frequency of each word a list of tweets

    arg:
    tweet_list contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionary with word as key and their frequency as value
    """

    def extractStopWords(file):
        """
        Return a list of stop words from file (one word per line)
        """
        
        stopList = []

        with open(file, encoding="UTF-8") as input:
            for line in input.readlines():
                word = line.strip()
                stopList.append(word)

        return stopList

    word_count = {}
    if stopList is not None:
        stopWords = extractStopWords(stopList)
    else:
        stopWords = []
        
    for tweet in tweet_list:
        for word in tweet["full_text"].split():
            word = word.lower()
            if word not in stopWords:
                word_count[word] = word_count.setdefault(word, 0)
                word_count[word] += 1

    return word_count


def countUserPerLang(file):
    """
    Count the number of user for each language

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with language as key and number of different user as value
    """

    with open(file, "r") as tweet_corpus:
        UserPerLang_count = {}
        
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            lang = tweet['lang']
            user = tweet['user_id']

            UserPerLang_count[lang] = UserPerLang_count.setdefault(lang, [])
            UserPerLang_count[lang].append(user)

        for key, value in UserPerLang_count.items():
            UserPerLang_count[key] = len(set(value))

    return UserPerLang_count


if __name__ == '__main__':
    #pprint(countUserPerLang("Alost_corpus.ndjson"))
    Charlie = advancedSearch("Alost_corpus.ndjson", lang="fr", contains=["charlie"])
    printTweets(Charlie)






