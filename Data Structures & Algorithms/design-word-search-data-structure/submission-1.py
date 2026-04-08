class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            offset = ord(c) - ord('a')
            if not cur.children[offset]:
                cur.children[offset] = TrieNode()
            cur = cur.children[offset]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, cur):
            if not cur:
                return False

            if i == n:
                return cur.endOfWord
            

            c = word[i]
            if c == '.':
                for child in cur.children:
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                offset = ord(c) - ord('a')
                if cur.children[offset]:
                    return dfs(i + 1, cur.children[offset])
                return False

        return dfs(0, self.root)




        
