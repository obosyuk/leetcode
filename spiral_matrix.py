class Solution:

    def go_right(self, matrix) -> list:
        result = []
        result = matrix[0]
        matrix[:] = matrix[1:]
        return result

    def go_bottom(self, matrix) -> list:
        result = []
        result = list(zip(*matrix))[-1]
        matrix[:] = list(zip(*list(zip(*matrix))[:-1]))
        return result

    def go_left(self, matrix) -> list:
        result = []
        result = matrix[-1]
        result = list(result)
        result.reverse()
        matrix[:] = matrix[:-1]
        return result

    def go_up(self, matrix) -> list:
        result = []
        result = list(zip(*matrix))[0]
        result = list(result)
        result.reverse()
        matrix[:] = list(zip(*list(zip(*matrix))[1:]))
        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        directions = ['right', 'bottom', 'left', 'up']
        result = []
        while matrix:
            for direction in directions:
                if matrix:
                    match direction:
                        case 'right':
                            result.extend(self.go_right(matrix))
                        case 'bottom':
                            result.extend(self.go_bottom(matrix))
                        case 'left':
                            result.extend(self.go_left(matrix))
                        case 'up':
                            result.extend(self.go_up(matrix))
                else:
                    break

        return result
