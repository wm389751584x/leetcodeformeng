class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word not in self.trie:
            self.trie.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if self.search(prefix): return True
        n = len(prefix)
        for word in self.trie:
            if len(prefix) <= len(word) and prefix == word[:n]:
                return True
        return False