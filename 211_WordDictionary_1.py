class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = dict()
            curr = curr.children[w]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        currLevel = [self.root]

        for w in word:
            nextLevel = []
            if w == '.':
                for node in currLevel:
                    nextLevel.extend(node.children.values())
            else:
                for node in currLevel:
                    nextLevel.append(node.children[w])

            if not nextLevel:
                return False
            
            currLevel = nextLevel

        for node in currLevel:
            if node.isEnd:
                return True
        return False
