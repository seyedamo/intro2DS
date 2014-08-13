import sys
import json
import re

if __name__ == '__main__':
    total = float(0)
    dict = {}
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        if line == "\n":
            continue
        decoded = json.loads(line)
        if "text" not in decoded:
            continue
        text = decoded['text'].encode('utf-8')
        word_list = text.split(" ")
        for word in word_list:
            word = re.sub(r"[^A-Za-z]*","",word)
            if len(word) == 0:
                continue
            total = float(total + 1)
            if word in dict:
                dict[word] = float(dict[word] + 1)
            else:
                dict[word] = float(1)
    for word in dict:
        print word + " " + str(dict[word]/total)    