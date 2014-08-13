import sys
import json
import re


def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    state_sents = {}
    for line in afinnfile:
  	    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	    scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        if line =='\n':
            continue
        tweet = json.loads(line)
        sentiment = 0
        if "place" not in tweet:
            continue
        place = tweet['place']
        if place is None:
            continue
        if "country_code" not in place:
            continue
        country_code = place['country_code'].encode('utf-8')
        if country_code != "US":
            continue
        if "full_name" not in place:
            continue
        full_name = place['full_name'].encode('utf-8')
        city, state = full_name.split(",")
        if len(state) == 0:
            continue
        if "text" in tweet:
            text = tweet['text'].encode('utf-8')
            for word in text.split(" "):
            	word = re.sub(r"[^a-zA-Z]*","",word)
            	if len(word) == 0:
            		continue
                if word in scores:
                    sentiment = sentiment + scores[word]
        if state in state_sents:
            state_sents[state] = state_sents[state] + int(sentiment)
        else:
            state_sents[state] = int(sentiment)

    sorted_states = sorted(state_sents, key = state_sents.get, reverse = True)
    
    if len(sorted_states) != 0:
        print sorted_states[0]

if __name__ == '__main__':
    main()
