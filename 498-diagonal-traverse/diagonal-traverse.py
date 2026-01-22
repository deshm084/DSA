class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        row = 0
        col = 0
        up = True
        for _ in range(rows * cols):
            result.append(matrix[row][col])
            if up:
                if col == cols - 1:
                    row += 1
                    up = False
                elif row == 0:
                    col += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:
                    col += 1
                    up = True
                elif col == 0:
                    row  +=  1
                    up = True
                else:
                    row += 1
                    col -= 1
        return result