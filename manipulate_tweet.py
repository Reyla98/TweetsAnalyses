# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:28:39 2020

@author: Laurane Castiaux
"""

import json
import re
from pprint import pprint


def dictMaxValues(dictionnary, n=100):
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
    

def printTweets(file):
    """
    Print the tweet_id followed by the full_text

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)
    """

    with open(file, encoding="UTF-8") as tweet_input:
        for line in tweet_input.readlines():
            tweet = json.loads(line)
            print("{} : {}".format(tweet["tweet_id"], tweet["full_text"]))


def countTags(file):
    """
    Count the frequence of each hashtag in a file containing tweets

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with hashtags as key and their frequency as value
    """

    with open(file, "r") as tweet_corpus:
        hashtags_count = {}
        
        for line in tweet_corpus.readlines():
            collected_tweet = json.loads(line)
            for tag in collected_tweet["entities.hashtags"]:
                # update hashtag_count
                hashtags_count[tag["text"]] = hashtags_count.setdefault(tag["text"], 0)
                hashtags_count[tag["text"]] += 1
    return hashtags_count


def searchTag(file, tag):
    """
    Prints the full_text of tweets in file containing tag
    Last line is the number of occurrences
    tag should include the symbol #
    """
    with open(file, "r") as tweet_corpus:
        n = 0
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            if tag in tweet["full_text"]:
                pprint(tweet["full_text"])
                n += 1
        print (n)


def countMention(file):
    """
    Count the frequence of each mention in a file containing tweets

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with mentions as key and their frequency as value
    """

    with open(file, "r") as tweet_corpus:
        mention_count = {}
        mention_pattern = re.compile("@[\w]+")
        
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            mentions = re.findall(mention_pattern, tweet["full_text"])

            for mention in mentions:
                # update mention_count
                mention_count[mention] = mention_count.setdefault(mention, 0)
                mention_count[mention] += 1
    return mention_count


def countTweetsPerUser(file):
    """
    Count the number of tweets of each user in a file containing tweets

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with user_screename as key and their frequency as value
    """

    with open(file, "r") as tweet_corpus:
        TweetsPerUser_count = {}
        
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            user = tweet['screen_name']

            # update TweetsPerUser_count
            TweetsPerUser_count[user] = TweetsPerUser_count.setdefault(user, 0)
            TweetsPerUser_count[user] += 1
    return TweetsPerUser_count


def countTweetPerDay(file):
    """
    Count the number of tweets per day in a file containing tweets

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with the date as key and the nuber of tweet as value
    """

    with open(file, "r") as tweet_corpus:
        TweetsPerDay_count = {}
        
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            date = re.match("(.{4}-.{2}-.{2}) .*", tweet['created_at']).group(1)

            # update TweetsPerDay_count
            TweetsPerDay_count[date] = TweetsPerDay_count.setdefault(date, 0)
            TweetsPerDay_count[date] += 1
    return TweetsPerDay_count


def countLang(file):
    """
    Count the number of tweets in each lang in a file containing tweets

    arg:
    file contains tweets in ndjson format (see Twitter's API doc for the
    format of tweets)

    Return a dictionnary with hashtags as key and their frequency as value
    """
    n = 0
    with open(file, "r") as tweet_corpus:
        lang_count = {}
        
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            lang_count["lang"] = lang_count.setdefault(tweet["lang"], 0)
            lang_count[tweet["lang"]] += 1
            n += 1
    print (n)
    return lang_count


def searchLang(file, lang):
    """
    Print the full_text of tweets in file written in language lang.
    Last line is the number of occurrences
    lang should be the two letter code of the language 
    """

    with open(file, "r") as tweet_corpus:
        n = 0
        for line in tweet_corpus.readlines():
            tweet = json.loads(line)
            if tweet["lang"] == lang:
                pprint(tweet["full_text"])
                n += 1
        print (n)


if __name__ == '__main__':
    pprint(len(countTweetsPerUser("Alost_corpus.ndjson")))

    #pprint(dictMaxValues(countWords("Alost_corpus.ndjson")))

    """
    AlostTags = countTags("ts_Alost.ndjson")
    AlostFirstTags = dictMaxValues(AlostTags,30)

    AlostMentions = countMention("Alost.ndjson")
    AlostFirstMentions = dictMaxValues(AlostMentions, 30)

    AlostTweetsPerUser = countTweetsPerUser("Alost_user.ndjson")
    AlostFirstTweetsPerUser = dictMaxValues(AlostTweetsPerUser, 10)

    CorpusTweetsPerDay = countTweetPerDay("Alost_corpus.ndjson")
    CorpusFirstTweetsPerDay = dictMaxValues(CorpusTweetsPerDay, len(CorpusTweetsPerDay))
    """

    #CorpusLang = countLang("Alost_corpus.ndjson")

    #pprint (AlostFirstTags)
    #pprint(AlostFirstMentions)
    #pprint(AlostFirstTweetsPerUser)
    #print (len(AlostTweetsPerUser))
    #pprint (CorpusTweetsPerDay)
    #pprint(CorpusLang)

    #searchLang("Alost_corpus.ndjson", "es")
    
    """
    #searchTag("Alost.ndjson", "#CarnavalAlost")
        #aalstcarnaval 223
        #aalstcarnival 29
        #CarnavalAlost 15

    #searchTag("Oilsjt.ndjson", "#Oilsjt")
    """