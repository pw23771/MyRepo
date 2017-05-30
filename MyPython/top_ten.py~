import sys
import json


def buildtweets(fp):
    tweets = []
    for line in fp:
	tweets.append(json.loads(line))
    return tweets

def tweethashtags(tweets):
    tweethashtags = {}
    ntweets = len(tweets)
    for i in range(ntweets):
	if "entities" in tweets[i]:
		if "hashtags" in tweets[i]["entities"]:
   			hashtags = tweets[i]["entities"]["hashtags"]
			for j in range(len(hashtags)):
				hashtag = hashtags[j]
				if "text" in hashtag:
    					hashtagtext = hashtag["text"].lower()
					if hashtagtext in tweethashtags:
						tweethashtags[hashtagtext] += 1
					else:
						tweethashtags[hashtagtext] = 1

    return tweethashtags

def main():

    tweet_file = open(sys.argv[1])
    
    tweets = buildtweets(tweet_file)

    hashtags = tweethashtags(tweets)

    from collections import OrderedDict
    orderedhashtags = OrderedDict(sorted(hashtags.items(), key=lambda x:x[1], reverse=True))

    rank = 1
    rankvalue = 0
    for k,v in orderedhashtags.items():
	if rankvalue == 0:
		rankvalue = v
	if rankvalue != v:
		rank += 1
		rankvalue = v
    	if rank > 10:
		break
	print "rank %s: %s %s"%(rank,k,v)


if __name__ == '__main__':
    main()
