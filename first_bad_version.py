# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start + 1 < end:
            pointer = (end + start) // 2
            if isBadVersion(pointer):
                end = pointer
            else:
                start = pointer
        return end

