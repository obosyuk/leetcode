class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word_list = []
        counter = len(s)

        while counter > 0:
            current_symbal = s[counter-1]
            if current_symbal == " " and last_word_list:
                return len(last_word_list)
            else:
                if current_symbal != " ":
                    last_word_list.append(current_symbal)
            counter -= 1

        return len(last_word_list)