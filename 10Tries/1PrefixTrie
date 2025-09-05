# Recursive solution. O(n) time per function call, where n is the length of a word.
# O(m) space where m is the total length of all words that were inserted

class PrefixTree:

    def __init__(self):
        self.isEnd = False
        self.charMap = {} #map letters to prefix Trees

    def insert(self, word: str) -> None:
        if word[0] not in self.charMap:
            self.charMap[word[0]] = PrefixTree() #add edge
        if len(word) == 1:
            self.charMap[word[0]].isEnd = True
        else:
            self.charMap[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if word[0] in self.charMap:
            if self.charMap[word[0]].isEnd and len(word) == 1:
                return True
            if len(word) != 1:
                return self.charMap[word[0]].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.charMap:
            return False
        if len(prefix) != 1:
            return self.charMap[prefix[0]].startsWith(prefix[1:])
        return True
        