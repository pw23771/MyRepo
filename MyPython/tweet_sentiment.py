import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def buildsent(fp):
    scores = {} # initialize an empty dictionay
    for line in fp:
	term, score = line.split("\t")
	scores[term] = int(score)	
    return scores

def buildtweets(fp):
    tweets = []
    for line in fp:
	tweets.append(json.loads(line))
    return tweets

def calculatesent(scores, tweets):
    tweetscores = []
    ntweets = len(tweets)
    for i in range(ntweets):
	tweetscore = 0
	if "text" in tweets[i]:
		tweet = tweets[i]["text"]
		# print tweet

		for word in tweet.split():
			word = word.strip("!,@,#,$,%,^,&,*,(,), ,+,=,-,_,{,},[,],\\,,\",\',.,<,>,:,;,?,/").lower() # need to use regExp to strip symbol characters
			sentscore = 0
			if word in scores:
				sentscore = scores.get(word)
		
			tweetscore += sentscore
			# print word,sentscore,tweetscore
	tweetscores.append(tweetscore)
    return tweetscores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = buildsent(sent_file)
    tweets = buildtweets(tweet_file)
    tweetscore = calculatesent(scores, tweets)
    # print scores.items()
    print "Number of tweets=%s, number of tweet scores=%s"%(len(tweets),len(tweetscore))
    print tweetscore
    

if __name__ == '__main__':
    main()
