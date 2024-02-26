import wikipedia

wikipedia.search("Golden State Warriors")
wikipedia.summary("Golden State Warriors")
golden_state_warriors_text = wikipedia.summary("Golden State Warriors")

from textblob import TextBlob

blob = TextBlob(golden_state_warriors_text)
blob.sentiment
