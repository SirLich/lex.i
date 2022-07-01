import requests
import json
import re
#import en
import random
import sys

#Enter some text: I own a dog names moose. I love him very much.
#I own a wienerwurst calumny European elk. I sex him very much.


def get_api_key():
    f = open("bristol/API_KEY.txt")
    key = f.readline().strip()
    f.close()
    return key

def build_url(word):
    url = 'http://words.bighugelabs.com/api/2/{}/{}/'.format(get_api_key(), word)
    return url

def strip_to_alpha(word):
    return re.sub(r'\W+', '', word).lower()

def fetch_synonym(word,part):
    out = word

    URL = build_url(word)
    response = requests.get(url = URL)

    synonyms = []
    for line in response.text.splitlines():
        marker, type, syn = line.split("|")
        if(marker == convert_semantic_marker_to_english(part) and type == "syn"):
            #print(syn)
            synonyms.append(syn)

    if(len(synonyms) > 0):
        out = random.choice(synonyms)

    return out


def process_sentance(sentance):
    out = ""
    semantic = en.sentence.tag(sentance)
    #touple_print(semantic)
    for tup in semantic:
        out += process_touple(tup)
    return out

def test_run():
    while(True):
        sentance = input("Enter some text: ")
        print(process_sentance(sentance))

def main(args):
    sentance = args[1]
    print(process_sentance(sentance))

main(sys.argv)
