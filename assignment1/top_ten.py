import json
import sys

if __name__ == '__main__':
    tweet_file = open(sys.argv[1])
    count_dict = {}
    for line in tweet_file:
        if line == "\n":
            continue
        tweet = json.loads(line)
        if "entities" not in tweet:
            continue
        entities = tweet['entities']
        if "hashtags" not in entities:
            continue
        hashtags = entities['hashtags']
        for tag in hashtags:
#            print tag['text'].encode('utf-8')
            tag_txt = tag['text']
            if tag_txt in count_dict:
                count_dict[tag_txt] = float(count_dict[tag_txt] + 1)
            else:
                count_dict[tag_txt] = float(1)
    sorted_words = sorted(count_dict, key = count_dict.get, reverse = True)
    for i in range(10):
        word = sorted_words[i]
        print word + " " + str(count_dict[word])
               