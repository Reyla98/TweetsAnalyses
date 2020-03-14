# TweetsAnalyses
Download and analyses on tweets


## create_ndjson.py
Use Tweepy or Twitterscraper to create a ndjson file with tweets that match the query.

## rm_duplicate.py
From an input ndjson file containing tweets, create a new file without duplicates.

    def rm_duplicates(file):
        """
        Creates a copy of file (contining tweets) without duplicated tweets

        arg:
        file is a file containing tweets in ndjson format with at least "twee_id" as parameter

        Create a new file (name = "no_dupl_"+filename without the lines that were repeated)
        """

## manipulate_tweet.py
Contain several functions to analyse various data from tweets registered in a ndjson file.

    def countTags(file):
        """
        Count the frequence of each hashtag in a file containing tweets

        arg:
        file is a file containing tweets in ndjson format (see Twitter's API doc
        for the format of tweets)

        Return a dictionnary with hashtags as key and their frequency as value
        """

    def dictMaxValues(dictionnary, n):
        """
        Return the n first elements of a dictionnary
        
        args:
        dictionnary is a dictionnary with int or float as values
        n is the number of wanted elements (n <= len(dictionnary))

        Return a list of tuples with the key and value of the n elements
        that have the biggest value.
        """
        
    def printTweets(file):
        """
        Print the tweet_id followed by the full_text

        arg:
        file contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)
        """
        
    def searchTag(file, tag):
        """
        Prints the full_text of tweets in file containing tag
        Last line is the number of occurrences
        tag should include the symbol #
        """

    def countMention(file):
        """
        Count the frequence of each mention in a file containing tweets

        arg:
        file contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)

        Return a dictionnary with mentions as key and their frequency as value
        """
   
    def countTweetsPerUser(file):
        """
        Count the number of tweets of each user in a file containing tweets

        arg:
        file contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)

        Return a dictionnary with user_screename as key and their frequency as value
        """
        
    def countTweetPerDay(file):
        """
        Count the number of tweets per day in a file containing tweets

        arg:
        file contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)

        Return a dictionnary with the date as key and the nuber of tweet as value
        """
        
    def countLang(file):
        """
        Count the number of tweets in each lang in a file containing tweets

        arg:
        file contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)

        Return a dictionnary with hashtags as key and their frequency as value
        """

    def searchLang(file, lang):
        """
        Print the full_text of tweets in file written in language lang.
        Last line is the number of occurrences
        lang should be the iso code of the language 
        """

## manipulate_tweet_v2.py
Enable to make advanced search on a ndjson file containing tweets, as well as all the same functions that are found in manipulate_tweet.py, except that thake list of tweets as input instead of file.
There are two more functions : countWords() and countUserPerLang(). Cf infra.

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

    def countWords(tweet_list, stopList=None):
        """
        Count the frequency of each word a list of tweets

        arg:
        tweet_list contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)

        Return a dictionary with word as key and their frequency as value
        """
NB: A list of stop word is available for English, French, Dutch, Spanish and Catalan in the "stopXX.txt" files.

    def countUserPerLang(file):
        """
        Count the number of user for each language

        arg:
        file contains tweets in ndjson format (see Twitter's API doc for the
        format of tweets)

        Return a dictionnary with language as key and number of different user as value
        """


## Alost.ndjson
Contain tweets that I collected related to the Aalst Carnival.

## stopXX.txt files
Contain stop words for specific languages. Those lists are used by the function countWords.
