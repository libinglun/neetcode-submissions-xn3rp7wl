class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        cur = self.root
        for c in word:
            offset = ord(c) - ord('a')
            if not cur.children[offset]:
                cur.children[offset] = TrieNode()
            cur = cur.children[offset]
        cur.endOfWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # form a trie given the list of words
        trie = Trie()
        for word in words:
            trie.addWord(word)

        # search the entire board via dfs given the trie
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        ans = set()
        def dfs(r, c, cur, path): 
            if cur.endOfWord:
                ans.add(path)

            if r < 0 or c < 0 or r >= row or c >= col or visited[r][c] or not cur:
                return
            

            visited[r][c] = True
            path += board[r][c]

            i = ord(board[r][c]) - ord('a')
            if cur.children[i]:
                dfs(r - 1, c, cur.children[i], path)
                dfs(r + 1, c, cur.children[i], path)
                dfs(r, c - 1, cur.children[i], path)
                dfs(r, c + 1, cur.children[i], path)

            visited[r][c] = False

        for i in range(row):
            for j in range(col):
                dfs(i, j, trie.root, "")
        return list(ans)


            







