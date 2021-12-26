# Implement the get_jokes() function that returns n jokes
# formed from three random words taken from three lists (one from each):

# nouns = ["car", "forest", "fire", "city", "house"]
# adverbs = ["today", "yesterday", "tomorrow", "the day before yesterday", "at night"]
# adjectives = ["cheerful", "bright", "green", "utopian", "soft"]

"""Import random"""

import random
from random import choice
from random import randrange

def get_jokes():
    joke_nouns = ["car", "forest", "fire", "city", "house"]
    joke_adverbs = ["today", "yesterday", "tomorrow", "the day before yesterday", "at night"]
    joke_adjectives = ["cheerful", "bright", "green", "utopian", "soft"]

    """Shuffle arguments at random"""
    random.shuffle(joke_nouns)
    random.shuffle(joke_adverbs)
    random.shuffle(joke_adjectives)

    """Stick lists together by zip()"""
    for nouns, adverbs, adjectives in zip(joke_nouns, joke_adverbs, joke_adjectives):
        print(f'{nouns} {adverbs} {adjectives}')

get_jokes()

