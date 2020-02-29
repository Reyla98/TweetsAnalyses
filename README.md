# TweetsAnalyses
Download and analyses on tweets


## create_ndjson.py
Use tweepy to create a ndjson file with tweets that match the query.

## rm_duplicate.py
Contain the function rm_duplicates(file)

    def rm_duplicates(file):
        """
        Creates a copy of file (contining tweets) without duplicated tweets

        arg:
        file is a file containing tweets in ndjson format with at least "twee_id" as parameter

        Create a new file (name = "no_dupl_"+filename without the lines that were repeated)
        """

## manipulate_tweet.py
Contain the functions countTags(file) and dictMaxValues(dictionnary, n)

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

## Alost.ndjson
Contain tweets that I collected related to the Aalst Carnival.
