import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def read_dict(fp):
    for line in fp:
        term,score = line.split('\t')
        dict[term] = float(score)
        

def create_new_sentiments(fp):
    for line in fp:
        if line =='\n':
            continue
        decoded = json.loads(line)
        sentiment = 0
        if "text" in decoded:
            text = decoded['text'].encode('utf-8')
            new_words = []
            for word in text.split(" "):
                word = re.sub(r"[^a-zA-Z]*", "", word)
                if len(word) == 0:
                    continue
                if word in dict:
                    sentiment = sentiment + dict[word]
#                    print word + " " + str(sentiment)
                else:
                    new_words.append(word)
#                    print "append new word " + word
            for word in new_words:
                if word in new:
                    new[word] = new[word] + float(sentiment)
#                    print word + " " + str(new[word])
                else:
                    new[word] = float(sentiment)
#                    print "add new word " + word + " " + str(new[word])
                if word in word_count:
                    word_count[word] = word_count[word] + 1
#                    print "count of new word " + word + " " + str(word_count[word])
                else:
                    word_count[word] = 1
#                    print "add " + word + " to count"
    for word in new:
        new[word] = new[word] / word_count[word]
#        print word + " " + str(new[word])
        dict[word] = new[word]            


def print_new_sentiments():
    for key in new:
        print key + " " + str(new[key])


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    read_dict(sent_file)
    sent_file.close()
    create_new_sentiments(tweet_file)
    print_new_sentiments()
#    evaluate_tweet(tweet_file)
    tweet_file.close()
    sent_file.close()

if __name__ == '__main__':
    global dict, new, word_count
    dict = {}
    new = {}
    word_count = {}
    main()
