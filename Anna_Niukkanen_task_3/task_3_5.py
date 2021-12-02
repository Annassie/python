# Implement the get_jokes() function that returns n jokes
# formed from three random words taken from three lists (one from each):

# nouns = ["car", "forest", "fire", "city", "house"]
# adverbs = ["today", "yesterday", "tomorrow", "the day before yesterday", "at night"]
# adjectives = ["cheerful", "bright", "green", "utopian", "soft"]

from random import choice

def get_jokes(*jokes):



    joke_nouns = ["car", "forest", "fire", "city", "house"]
    joke_adverbs = ["today", "yesterday", "tomorrow", "the day before yesterday", "at night"]
    joke_adjectives = ["cheerful", "bright", "green", "utopian", "soft"]


    joke = choice(joke_nouns)

    for nouns, adverbs, adjectives in zip(joke_nouns, joke_adverbs, joke_adjectives):
        print(f'{joke}')


get_jokes()


