from app.autocomplete.trie import Trie
from app.autocomplete.ngram import NGramModel
from app.autocomplete.ranking import SuggestionRanker
from app.preprocessing.vocabulary_builder import VocabularyBuilder
from app.autocorrect.spell_checker import SpellChecker

class AutoCompleteEngine:

def init(self, corpus_path):
self.trie = Trie()
self.ngram = NGramModel()
self.word_frequency = {}

self._load_vocabulary(corpus_path)

self.spell_checker = SpellChecker(self.word_frequency)
self.ranker = SuggestionRanker(self.word_frequency)

def _load_vocabulary(self, corpus_path):
builder = VocabularyBuilder(corpus_path)

self.word_frequency, words = builder.build()

# Insert words into Trie with frequency
for word, frequency in self.word_frequency.items():
self.trie.insert(word, frequency)

# Train N-Gram model
self.ngram.train(words)

# Initialize ranker
self.ranker = SuggestionRanker(self.word_frequency)

def suggest(self, word):

# Get suggestions from Trie
results = self.trie.starts_with(word)
suggestions = [item["word"] for item in results]

# If no suggestions, try autocorrect
if not suggestions:

corrected = self.spell_checker.correct(word)

results = self.trie.starts_with(corrected)
suggestions = [item["word"] for item in results]

suggestions = self.ranker.rank(suggestions)

return corrected, suggestions

suggestions = self.ranker.rank(suggestions)

return None, suggestions

def predict_next_word(self, word):
return self.ngram.predict(word)

def suggest_sentence(self, sentence):

sentence = sentence.strip().lower()

if not sentence:
return []

words = sentence.split()
last_word = words[-1]

results = self.trie.starts_with(last_word)

suggestions = [
item["word"]
for item in results
]

suggestions = self.ranker.rank(suggestions)

completed_sentences = []

for suggestion in suggestions:
new_sentence = words[:-1] + [suggestion]
completed_sentences.append(" ".join(new_sentence))

return completed_sentences
