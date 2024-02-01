class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word_list = []

        prev_symb = ""
        for symb in s:
            if symb != " ":
                if prev_symb == " ":
                    last_word_list = [symb]
                else:
                    last_word_list.append(symb)
            prev_symb = symb

        return len(last_word_list)
