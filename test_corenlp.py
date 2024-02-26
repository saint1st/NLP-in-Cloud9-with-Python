from nlplogic.corenlp import search_wikipedia, summarise_wikipedia, get_text_blob, get_phrases

def test_get_phrase():
    assert 'golden state' in get_phrases("Golden State Warriors")