class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # convert magazine to hash map
        magazineMap = {}
        for i in magazine:
            if i in magazineMap:
                magazineMap[i] += 1
            else:
                magazineMap[i] = 1

        # check
        for g in ransomNote:
            if g in magazineMap:
                if magazineMap[g] == 1:
                    del magazineMap[g]
                else:
                    magazineMap[g] -= 1
            else:
                return False

        return True
