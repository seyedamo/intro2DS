import sys
import json
import re


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
  	    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	    scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        if line =='\n':
            continue
        decoded = json.loads(line)
        sentiment = 0
        if "text" in decoded:
            text = decoded['text'].encode('utf-8')
            for word in text.split(" "):
            	word = re.sub(r"[^a-zA-Z]*","",word)
            	if len(word) == 0:
            		continue
                if word in scores:
                    sentiment = sentiment + scores[word]
        print sentiment

if __name__ == '__main__':
    main()
