class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list_reversed = reversed(s_list)
        return " ".join(s_list_reversed)