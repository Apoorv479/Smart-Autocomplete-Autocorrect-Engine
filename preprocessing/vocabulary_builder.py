import re
from collections import Counter

class VocabularyBuilder:
def init(self, corpus_path):
self.corpus_path = corpus_path

def build(self):
with open(self.corpus_path, "r", encoding="utf-8") as file:
text = file.read().lower()

words = re.findall(r"\b[a-zA-Z0-9']+\b", text)

word_frequency = Counter(words)

return word_frequency, words
