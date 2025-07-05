words = ["231", "20", "-45", "99"]
map(int, words)
words
words = list(map(int, words))
words

def changePerson(sentence):
    """Replaces first person pronouns with second person person pronouns."""
    words = sentence.split( )
    replyWords = []
    for word in words:
#        replyWords.append(replacements.get(word, word))
#    return " ".join(replyWords)

#def changePerson(sentence):
#    """Replaces first person pronouns with second person pronouns."""
#    def getWord(word):
#        return replacements.get(word, word)
#    return " ".join(map(getWord, sentence.split()))    