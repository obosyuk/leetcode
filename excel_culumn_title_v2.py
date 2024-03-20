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
        charShift = 65
        numberOfChars = 26
        resultList = []
        quotient = columnNumber

        while quotient:
            quotient, remainder = divmod(quotient - 1, numberOfChars)
            resultList.append(chr(remainder + charShift))

        return "".join(reversed(resultList))





