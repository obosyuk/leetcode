class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                p1_ready_to_check = False
            else:
                p1_ready_to_check = True

            if not s[p2].isalnum():
                p2 -= 1
                p2_ready_to_check = False
            else:
                p2_ready_to_check = True

            if p1_ready_to_check and p2_ready_to_check:
                if s[p1].lower() != s[p2].lower():
                    return False
                p1 += 1
                p2 -= 1

        return True
