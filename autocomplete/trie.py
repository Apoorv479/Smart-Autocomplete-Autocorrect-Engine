class TrieNode:
def init(self):
self.children = {}
self.is_end_of_word = False
self.frequency = 0

class Trie:
def init(self):
self.root = TrieNode()

def insert(self, word, frequency=1):
current = self.root

for char in word:
if char not in current.children:
current.children[char] = TrieNode()

current = current.children[char]

current.is_end_of_word = True
current.frequency = frequency

def search(self, word):
current = self.root

for char in word:
if char not in current.children:
return False

current = current.children[char]

return current.is_end_of_word

def starts_with(self, prefix):
current = self.root

for char in prefix:
if char not in current.children:
return []

current = current.children[char]

words = []
self._dfs(current, prefix, words)

return words

def _dfs(self, node, current_word, words):
if node.is_end_of_word:
words.append(
{
"word": current_word,
"frequency": node.frequency
}
)

for char, child in node.children.items():
self._dfs(child, current_word + char, words)
