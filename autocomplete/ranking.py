class SuggestionRanker:

def init(self, word_frequency):
self.word_frequency = word_frequency

def rank(self, suggestions):

return sorted(
suggestions,
key=lambda word: (
-self.word_frequency.get(word, 0),
len(word),
word
)
)
