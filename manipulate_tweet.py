# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:28:39 2020

@author: laura
"""

import json
import re
from pprint import pprint


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


if __name__ == '__main__':

    AlostTags = countTags("Alost.ndjson")
    AlostFirstTags = dictMaxValues(AlostTags,30)

    AlostMentions = countMention("Alost.ndjson")
    AlostFirstMentions = dictMaxValues(AlostMentions, 30)


    #pprint (AlostFirstTags)
    #pprint(AlostFirstMentions)

    #searchTag("Alost.ndjson", "#CarnavalAlost")
    #aalstcarnaval 223
    #aalstcarnival 29
    #CarnavalAlost 15

    #searchTag("Oilsjt.ndjson", "#Oilsjt")

