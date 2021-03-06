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

def calculatenonsent(scores, tweets):
    tweetscores = []
    nonsentscores = {}
    ntweets = len(tweets)
    for i in range(ntweets):
	tweetscore = 0
	nonsentterm = []
	ncount = 0
	if "text" in tweets[i]:
		tweet = tweets[i]["text"]
		# print tweet

		for word in tweet.split():
			word = word.strip("!,@,#,$,%,^,&,*,(,), ,+,=,-,_,{,},[,],\\,,\",\',.,<,>,:,;,?,/").lower() # need to use regExp to strip symbol characters
			sentscore = 0
			if word in scores:
				sentscore = scores.get(word)
				ncount += 1
			else:
				nonsentterm.append(word) #Calculate the score
		
			tweetscore += sentscore
			# print word,sentscore,tweetscore
	if ncount > 0:
		for i in range(len(nonsentterm)):
			wordnon = nonsentterm[i]
			if wordnon in nonsentscores:
				nonsentscores[wordnon]+=tweetscore/ncount
				nonsentscores[wordnon] = nonsentscores[wordnon]/2.0
			else:
				nonsentscores[wordnon] = tweetscore/ncount
	#tweetscores.append(tweetscore)
    return nonsentscores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = buildsent(sent_file)
    tweets = buildtweets(tweet_file)
    nontermscores = calculatenonsent(scores, tweets)
    # print scores.items()
    #print "Number of tweets=%s, number of tweet scores=%s"%(len(tweets),len(tweetscore))
    for key,value in nontermscores.items():
    	print key.encode('utf-8'),value
    

if __name__ == '__main__':
    main()
