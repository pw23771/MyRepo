import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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

def happiest_state(scores, tweets):
    statescores = {}
    ntweets = len(tweets)
    for i in range(ntweets):
	tweetscore = 0
	#calculate tweet score
	if "text" in tweets[i]:
		tweet = tweets[i]["text"]
		# print tweet

		for word in tweet.split():
			word = word.strip("!,@,#,$,%,^,&,*,(,), ,+,=,-,_,{,},[,],\\,,\",\',.,<,>,:,;,?,/").lower() # need to use regExp to strip symbol characters
			sentscore = 0
			if word in scores:
				sentscore = scores.get(word)
		
			tweetscore += sentscore
	# find the state
	if "user" in tweets[i]:
		if  "location" in tweets[i]["user"]:
			if tweets[i]["user"]["location"] != "":   
    				location = tweets[i]["user"]["location"].lower()
				for k,v in states.items():
					if location.find(v.lower()) > -1:
						if k in statescores:
							statescores[k] += tweetscore
						else:
							statescores[k] = tweetscore

    return statescores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = buildsent(sent_file)
    tweets = buildtweets(tweet_file)
    happieststatescore = happiest_state(scores, tweets)

    from collections import OrderedDict
    happieststates = OrderedDict(sorted( happieststatescore.items(), key=lambda x:x[1], reverse=True))

    rank = 1
    rankvalue = 0
    for k,v in happieststates.items():
	if rankvalue == 0:
		rankvalue = v
	if rankvalue != v:
		rank += 1
		rankvalue = v
    	#if rank > 10:
	#	break
	print "rank %s: %s %s"%(rank,k,v)

    # print scores.items()
    #print "Number of tweets=%s, number of tweet scores=%s"%(len(tweets),len(tweetscore))
    #print tweetscore
    

if __name__ == '__main__':
    main()
