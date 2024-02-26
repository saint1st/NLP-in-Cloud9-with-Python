import wikipedia
from textblob import TextBlob


def search_wikipedia(name):
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarise_wikipedia(name):
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):

    blob = TextBlob(text)
    return blob


def get_phrases(name):

    text = summarise_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases

    return phrases
