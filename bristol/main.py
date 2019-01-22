#!/usr/bin/python

import requests
import json
import re
import en
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
    url = 'http://words.bighugelabs.com/api/2/{}/{}/'.format(get_api_key(),word)
    return url

def strip_to_alpha(word):
    return re.sub(r'\W+', '', word).lower()

#Credit: https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913
def is_adjective(word):
    word = " " + word + " "
    if word in open('adjectives.txt').read():
        return True
    return False

def process_touple(tup):
    word = tup[0]
    part = tup[1]
    if(part in (".",",",":")):
        return word
    if(part in ("VB","VBD","VBG","VBP","VBZ")):
        return " " + fetch_synonym(word,part)

    if(part in ("NN","NNP","NNPS","NNS","NP","JJ")):
        return " " + fetch_synonym(word,part)
    return " " + word

def fetch_synonym(word,part):
    out = word

    # #Verb specific
    # if(part in ("VB","VBD","VBG","VBP","VBZ")):
    #     tense = en.verb.tense(word)
    #     word = en.verb.infinitive(word)
    #     if(word == "be"):
    #         return out

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

    # #Verb specific
    # if(part in ("VB","VBD","VBG","VBP","VBZ") and tense):
    #     out = en.verb.conjugate(out,tense)

    return out

def convert_semantic_marker_to_english(sem):
    if(sem in ("VB","VBD","VBP","VBZ")):
        return "verb"
    else:
        return "noun"

def process_sentance(sentance):
    out = ""
    semantic = en.sentence.tag(sentance)
    #touple_print(semantic)
    for tup in semantic:
        out += process_touple(tup)
    return out


def touple_print(semantic):
    for tup in semantic:
        print(tup[0] + " " + tup[1])

def test_run():
    while(True):
        sentance = raw_input("Enter some text: ")
        print(process_sentance(sentance))

def main(args):
    sentance = args[1]
    print process_sentance(sentance)

main(sys.argv)
