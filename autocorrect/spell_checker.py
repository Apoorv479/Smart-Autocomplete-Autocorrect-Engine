import string

class SpellChecker:

def init(self, word_frequency):
self.word_frequency = word_frequency
self.vocabulary = set(word_frequency.keys())

def correct(self, word):

if word in self.vocabulary:
return word

candidates = (
self.known([word]) or
self.known(self.edits1(word)) or
self.known(self.edits2(word)) or
[word]
)

return max(
candidates,
key=lambda w: self.word_frequency.get(w, 1)
)

def known(self, words):
return set(w for w in words if w in self.vocabulary)

def edits1(self, word):

letters = string.ascii_lowercase

splits = [
(word[:i], word[i:])
for i in range(len(word) + 1)
]

deletes = [
L + R[1:]
for L, R in splits
if R
]

transposes = [
L + R[1] + R[0] + R[2:]
for L, R in splits
if len(R) > 1
]

replaces = [
L + c + R[1:]
for L, R in splits
if R
for c in letters
]

inserts = [
L + c + R
for L, R in splits
for c in letters
 ]

return set(
deletes +
transposes +
replaces +
inserts
)

def edits2(self, word):
return (
e2
for e1 in self.edits1(word)
for e2 in self.edits1(e1)
)
