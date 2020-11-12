from nltk.corpus import wordnet as wn


def get_meaning(word):
    synsets=wn.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return

def get_synonyms(word):
    synonyms=[]
    synsets=wn.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma:
                synonyms.append(lemma.name())
    return set(synonyms)

def get_antonyms(word):
    antonyms = []
    synsets = wn.synsets(word)
    for synset in synsets:
        lemmas = synset.lemmas()
        for lemma in lemmas:
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return set(antonyms)



