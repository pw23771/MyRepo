import sys
import json


def buildtweets(fp):
    tweets = []
    for line in fp:
	tweets.append(json.loads(line))
    return tweets

def calculatefrequency(tweets):
    termfrequency = {}
    ntweets = len(tweets)
    ntotalterms = 0
    for i in range(ntweets):
	term = []
	ncount = 0
	if "text" in tweets[i]:
		tweet = tweets[i]["text"]
		# print tweet

		for word in tweet.split():
			word = word.strip("!,@,#,$,%,^,&,*,(,), ,+,=,-,_,{,},[,],\\,,\",\',.,<,>,:,;,?,/").lower() # need to use regExp to strip symbol characters
			if word in termfrequency:
				termfrequency[word] += 1
			else:
				termfrequency[word] = 1
			ntotalterms += 1
		
    return (ntotalterms,termfrequency)

def main():
    tweet_file = open(sys.argv[1])
    
    tweets = buildtweets(tweet_file)
    totalterms, termfrequency = calculatefrequency(tweets)

    for key,value in termfrequency.items():
    	print key.encode('utf-8'),value/(totalterms*1.0)
    print totalterms
    

if __name__ == '__main__':
    main()
