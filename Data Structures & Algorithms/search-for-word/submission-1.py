class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_row = len(board)
        num_col = len(board[0])
        start = []
       
                    
        visited = [[0 for _ in range(num_col)] for _ in range(num_row)]          
        def dfs(row, col, i):
            if i == len(word):
                return True

            if row < 0 or col < 0 or row >= num_row or col >= num_col or visited[row][col] or board[row][col] != word[i]:
                return False

            visited[row][col] = 1
            res = dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1)

            visited[row][col] = 0

            return res       
        
                    
        for i in range(num_row):
            for j in range(num_col):
                if dfs(i, j, 0):
                    return True

        return False