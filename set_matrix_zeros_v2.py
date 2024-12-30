class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        columns_to_zero = set()

        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if col == 0:
                    rows_to_zero.add(row_idx)
                    columns_to_zero.add(col_idx)

        for row_idx in rows_to_zero:
            matrix[row_idx] = [0 for _ in range(len(matrix[0]))]

        for row_idx, rows in enumerate(matrix):
            if row_idx in rows_to_zero:
                matrix[row_idx] = [0 for _ in range(len(matrix[0]))]
            elif columns_to_zero:
                for col_idx in columns_to_zero:
                    matrix[row_idx][col_idx] = 0


