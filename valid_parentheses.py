class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses = (('(', ')'), ('{', '}'), ('[', ']'))

        open_parentheses_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        # closed_parentheses_map = {
        #     ')': '(',
        #     '}': '{',
        #     ']': '[',
        # }

        unclosed_perentheses = []
        for i in s:
            if i in open_parentheses_map.keys():
                unclosed_perentheses.append(i)
            else:
                if unclosed_perentheses and open_parentheses_map[unclosed_perentheses[-1]] == i:
                    unclosed_perentheses.pop()
                else:
                    return False
        if not unclosed_perentheses:
            return True
        return False
