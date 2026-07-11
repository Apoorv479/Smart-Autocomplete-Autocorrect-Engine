from collections import defaultdict, Counter

class NGramModel:

def init(self):
self.bigram = defaultdict(Counter)

def train(self, words):

for i in range(len(words) - 1):
current = words[i]
next_word = words[i + 1]

self.bigram[current][next_word] += 1

def predict(self, word, top_k=5):

if word not in self.bigram:
return []

return [
next_word
for next_word, _ in
self.bigram[word].most_common(top_k)
]
