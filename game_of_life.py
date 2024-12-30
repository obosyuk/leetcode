from itertools import product


class Solution:
    def getNumberOfLiveNeighbors(self, cell: List[int], board: List[List[int]]) -> int:
        rows = []
        cols = []

        if cell[0] - 1 >= 0:
            rows.append(cell[0] - 1)

        rows.append(cell[0])

        if cell[0] + 1 <= len(board) - 1:
            rows.append(cell[0] + 1)

        if cell[1] - 1 >= 0:
            cols.append(cell[1] - 1)

        cols.append(cell[1])

        if cell[1] + 1 <= len(board[0]) - 1:
            cols.append(cell[1] + 1)

        neighbors = list(product(rows, cols))

        liveNeighbors = list((r, c) for r, c in neighbors if board[r][c] == 1 and (r != cell[0] or c != cell[1]))

        return len(liveNeighbors)

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        columnsToUpdate = []
        # neigbors = dict()

        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                liveNeighbors = self.getNumberOfLiveNeighbors([row_idx, col_idx], board)
                if col == 1:
                    if liveNeighbors < 2:
                        nextState = 0
                        columnsToUpdate.append((row_idx, col_idx, nextState))
                    elif liveNeighbors in (2, 3):
                        pass
                    else:
                        nextState = 0
                        columnsToUpdate.append((row_idx, col_idx, nextState))
                else:
                    if liveNeighbors == 3:
                        nextState = 1
                        columnsToUpdate.append((row_idx, col_idx, nextState))

        for row_idx, col_idx, state in columnsToUpdate:
            board[row_idx][col_idx] = state

