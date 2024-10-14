class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        rest = t
        for x in s:
            is_found = False
            for count, y in enumerate(rest):
                if x == y:
                    is_found = True
                    rest = rest[count + 1:]
                    break

            if not is_found:
                return False

        return True


