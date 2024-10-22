class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False

        pattern_dict = dict()
        s_dict = dict()

        for idx, pattern_letter in enumerate(pattern):
            s_word = s_list[idx]

            if pattern_letter in pattern_dict:
                if pattern_dict[pattern_letter] != s_list[idx]:
                    return False
            else:
                if s_word not in s_dict:
                    pattern_dict[pattern_letter] = s_word
                    s_dict[s_word] = pattern_letter
                else:
                    return False

        return True