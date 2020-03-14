from manipulate_tweet_v2 import *

def NL():
    def VRT():
        TweetsVRT = []
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", mentions=["vrtnws"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", screen_name="vrtnws"))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", mentions=["VTMNIEUWS"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", hashtags=["vrtnws"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", contains=["vrt"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", contains=["zevende", "dag"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", hashtags=["zevendedag"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", mentions=["De7deDag"]))
        TweetsVRT.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", hashtags=["7Dag"]))

        #remove duplicates
        dic = {}
        for tweet in TweetsVRT:
            if tweet["tweet_id"] in dic:
                TweetsVRT.remove(tweet)
            else:
                dic[tweet["tweet_id"]] = 1

        return TweetsVRT


    def HLN():
        tweetsHLN = []
        tweetsHLN.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", screen_name="HLN_BE"))
        tweetsHLN.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", mentions=["HLN_BE"]))
        tweetsHLN.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", hashtags=["hln"]))
        tweetsHLN.extend(advancedSearch("Alost_corpus.ndjson", lang="nl", hashtags=["HLN"]))

        for tweet in TweetsHLN:
            if tweet["tweet_id"] in dic:
                TweetsHLN.remove(tweet)
            else:
                dic[tweet["tweet_id"]] = 1

        return tweetsHLN
                

    NL = advancedSearch("Alost_corpus.ndjson", lang="nl")
    #pprint(dictMaxValues(countTags(NL)))

    NLVRT = VRT()
    #pprint (dictMaxValues(countWords(NLVRT, "stopnl.txt"), 300))
    printTweets(NLVRT)

    print("\n------------------\n")

    NLHLN = HLN()
    #printTweets(NLVRT)
    #pprint (dictMaxValues(countWords(NLHLN, "stopnl.txt"), 300))
    printTweets(NLHLN)

    def Unesco():
        n = 0
        for tweet in NL:
            if re.search("[uU][nN][eE][sS][cC][oO]", tweet["full_text"]) is not None:
                n += 1
        print (n)
    #Unesco()   #56


def FR():
    tweetsFR = []
    tweetsFR.extend(advancedSearch("Alost_corpus.ndjson", lang="fr"))

    #pprint(dictMaxValues(countWords(tweetsFR, "stopfr.txt"), 300))

    def antisémitisme():
        n = 0
        m = 0
        for tweet in tweetsFR:
            if re.search(".?[Aa]nti ?[sS][ée]mi", tweet["full_text"]) is not None:
                n += 1
            elif re.search("[jJ]ui[fv]", tweet["full_text"]) is not None:
                m += 1
            else:
                printTweets([tweet])
        print (n, m)
    #antisémitisme() #260, 101

    def Unesco():
        n = 0
        for tweet in tweetsFR:
            if re.search("[uU][nN][eE][sS][cC][oO]", tweet["full_text"]) is not None:
                n += 1
        print (n)
    #Unesco()   #35


def ES():
    tweetsES = []
    tweetsES.extend(advancedSearch("Alost_corpus.ndjson", lang="es"))

    #pprint(dictMaxValues(countTags(tweetsES)))

    #pprint (dictMaxValues(countWords(tweetsES, "stopes.txt"), 300))

    def Unesco():
        n = 0
        for tweet in tweetsES:
            if re.search("[uU][nN][eE][sS][cC][oO]", tweet["full_text"]) is not None:
                n += 1
                printTweets([tweet])
        print (n)
    #Unesco()

    #printTweets(tweetsES)


def CA():
    tweetsCA = []
    tweetsCA.extend(advancedSearch("Alost_corpus.ndjson", lang="ca"))

    #pprint(dictMaxValues(countTags(tweetsCA)))

    #pprint (dictMaxValues(countWords(tweetsCA, "stopca.txt"), 300))

    def Puigdemont():
        n = 0
        for tweet in tweetsCA:
            if re.search("[Pp]uigdemont", tweet["full_text"]) is not None:
                n += 1
                printTweets([tweet])
                print(tweet["user_id"])
        print(n)
    Puigdemont()

    #printTweets(tweetsCA)


def EN():
    tweetsEN = []
    tweetsEN.extend(advancedSearch("Alost_corpus.ndjson", lang="en"))

    pprint (dictMaxValues(countWords(tweetsEN, "stopen.txt"), 300))

    #printTweets(tweetsEN)

if __name__ == "__main__":

    #NL()

    #FR()

    #ES()
    #CA()

    EN()

