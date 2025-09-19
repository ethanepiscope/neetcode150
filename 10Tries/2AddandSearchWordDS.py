# Recursive solution. O(n) time per call to addWord and search, where n is the length of the word.
# O(m) space, where m is the total length of words added.

class WordDictionary:

    def __init__(self):
        self.d = {} #map letters to children WordDictionary's
        self.isEnd = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.isEnd = True
            return
        if word[0] not in self.d:
           self.d[word[0]] = WordDictionary()
        self.d[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.isEnd
        if word[0] == '.':
            acc = False
            for wd in self.d.values():
                acc |= wd.search(word[1:])
            return acc
        if word[0] not in self.d:
            return False
        return self.d[word[0]].search(word[1:])
