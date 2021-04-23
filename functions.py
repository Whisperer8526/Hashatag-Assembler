import random
from enum import IntEnum


def choose_phrase():
    phrase = input("Which phrase are you looking for?: ")
    hashtagsOutput = [s for s in hashtagsUnique if phrase in s]
    return hashtagsOutput


def how_many_hashtags(hashtagsOutput):
    try:
        numberOfHashtags = int(input("How many hashtags do you need?: "))
        hashtagsChosen = random.sample(hashtagsOutput, numberOfHashtags)
    except ValueError:
        print("This Hashtag has only", len(hashtagsOutput), "positions. They have been added.")
        hashtagsChosen = random.sample(hashtagsOutput, len(hashtagsOutput))
        for hashtag in hashtagsChosen:
            hashtagList.append(hashtag)
        return len(hashtagsOutput)
    else:
        for hashtag in hashtagsChosen:
            hashtagList.append(hashtag)
        return numberOfHashtags
