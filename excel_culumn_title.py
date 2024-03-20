# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        shift = 64
        numberOfChars = 26

        remainder = columnNumber
        resultList = []
        while True:
            if remainder <= numberOfChars:
                resultList.append(chr(remainder + shift))
                break

            _remainder = remainder // numberOfChars  # 28 // 26 => 1
            modulo = remainder % numberOfChars

            if modulo == 0:
                _remainder -= 1
                modulo = numberOfChars

            resultList.append(chr(modulo + shift))  # 28 % 26 => 2

            if _remainder < 1:
                break
            else:
                remainder = _remainder

        return str("".join(list(reversed(resultList))))


