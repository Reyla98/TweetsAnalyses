import json

def rm_duplicates(file):
    """
    creates a copy of file (contining tweets) without duplicated tweets

    arg:
    file is a file containing tweets in ndjson format with at least
    "twee_id" as parameter

    Creates a new file (name = "no_dupl_"+filename without the lines
    that were repeated)
    """

    with open(file, "r") as tweet_input:
        with open("no_dupl_{}".format(file), "w") as tweet_output:
        
            tweet_id = {}
            for line in tweet_input.readlines():
                
                #try to loads one line in json format
                try:
                    collected_tweet = json.loads(line)

                #print the first line that is misencoded if any
                except:
                    print("Problem with line"+line)
                    break

                #if tweet not already copied in tweet_output, it is written
                if collected_tweet["tweet_id"] not in tweet_id:
                    tweet_output.write(line)
                    tweet_id[collected_tweet["tweet_id"]] = 1

rm_duplicates("test.ndjson")
