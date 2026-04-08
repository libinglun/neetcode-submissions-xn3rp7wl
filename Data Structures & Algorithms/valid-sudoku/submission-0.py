class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def contain_duplicates(digits: list[str]):
            digits = [digit for digit in digits if digit != '.']
            print(digits)
            print(len(digits))
            print(len(set(digits)))
            return len(digits) != len(set(digits))

        for row in range(len(board)):
            if contain_duplicates(board[row]):
                print('ROW')
                print(board[row])
                return False

        for column in range(len(board)):
            if contain_duplicates([board[row][column] for row in range(len(board))]):
                print('COL')
                return False

        centers = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
        shift = [(-1, 0), (-1, -1), (-1, 1), (0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
        for center in centers:
            row, col = center
            sub_box = [board[row + i][col + j] for i, j in shift]
            if contain_duplicates(sub_box):
                print('BOX')
                return False

        return True
        