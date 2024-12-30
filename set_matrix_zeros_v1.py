class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if col == 0:
                    rows.add(row_idx)
                    columns.add(col_idx)

        for row_idx in rows:
            matrix[row_idx] = [0 for _ in range(len(matrix[0]))]

        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if col_idx in columns:
                    matrix[row_idx][col_idx] = 0

