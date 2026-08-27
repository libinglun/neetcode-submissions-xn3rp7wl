class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start, end = 0, len(matrix) - 1

        while start < end:
            for i in range(end - start):
                topleft = matrix[start][start + i]

                # bottom left to top left
                matrix[start][start + i] = matrix[end - i][start]

                # bottom right to bottom left
                matrix[end - i][start] = matrix[end][end - i]

                # top right to bottom right
                matrix[end][end - i] = matrix[start + i][end]

                # top left to top right
                matrix[start + i][end] = topleft
            start += 1
            end -= 1