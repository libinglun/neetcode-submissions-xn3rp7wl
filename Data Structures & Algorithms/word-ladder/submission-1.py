class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        ans = 1
        visited = set()
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return ans
                for i in range(len(node)):
                    for c in range(27):
                        if chr(97 + c) == node[i]:
                            continue
                        nei = node[:i] + chr(97 + c) + node[i+1:]
                        if nei in wordList and nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            ans += 1

        return 0