class Solution:
    def getNextLetterLocation(
            board: List[List[str]], cur_letter_loc: tuple[int, int], target_letter: str
    ) -> Optional[tuple]:
        """
        Returns the first suitable letter (its location).
        Otherwise returns None.
        """
        lines = len(board)
        columns = len(board[0])

        adj_loc_line = cur_letter_loc[0]
        adj_loc_col = cur_letter_loc[1]

        # check the same line
        try:
            letter = board[adj_loc_line][adj_loc_col + 1]
            if letter == target:
                return (adj_loc_line, adj_loc_col + 1)
        except:
            pass

        try:
            letter = board[adj_loc_line][adj_loc_col - 1]
            if letter == target:
                return (adj_loc_line, adj_loc_col - 1)
        except:
            pass

        # check the same column
        try:
            letter = board[adj_loc_line + 1][adj_loc_col]
            if letter == target:
                return (adj_loc_line + 1, adj_loc_col)
        except:
            pass

        try:
            letter = board[adj_loc_line - 1][adj_loc_col]
            if letter == target:
                return (adj_loc_line - 1, adj_loc_col)
        except:
            pass

    def areNeighbors(loc1: tuple[int, int], loc2: tuple[int, int]) -> bool:
        pass

    def getAdjace(self, letter_idx: int) -> bool:
        word = ""
        return word + self.getRestOfTheWord()

    def getNextLocation(
            word: str, letters_dict, letter_idx: int, used_letters: set[tuple[int, int]]
    ) -> Optional[tuple[int, int]]:
        results = []
        for cur_location in letters_dict:

    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1. Find the first letter of the word in the grid
        # 2. Check if it's alredy used
        # 3. If not, check adjacent cells for other letters
        # 4. Try searching until we find the word
        # 5. If there is no more unchecked letters, return False

        # letters_dict = {
        #     'A': [{'location': (0,1), 'adjacents': [{}, {}, {}, {}]}]
        # }

        # checked_paths = set()
        # used_letters = set() # {(0,1), (1,1)}

        letters_dict = dict()
        for line_num, line_val in enumerate(board):
            for col_num, col_val in enumerate(line_val):
                letter = board[line_num][col_num]
                if letter in word:
                    letter_loc = (line_num, col_num)
                    if letter in letters_dict:
                        letters_dict[letter].append(letter_loc)
                    else:
                        letters_dict[letter] = [letter_loc]

        used_letters = set()
        found_letters = list()

        prev_location = None

        for target_letter in word:
            if target_letter in letters_dict:
                for target_location in letters_dict[target_letter]:
                    # check if this location is neiboring to previous one
                    # check if it is alredy used
                    pass
                    # get adjacents for this target location
                    # if self.areNeighbors(target_location, )
            else:
                return False

            # find all ways

        # for letter in word:
        #     for line_num, line_val in enumerate(board):
        #         for col_num, col_val in enumeraete(line):
        #             pass



