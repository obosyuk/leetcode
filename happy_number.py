class Solution:
    def isHappy(self, n: int) -> bool:
        happy_number = n
        seen_digits = set()

        while happy_number != 1 and happy_number not in seen_digits:
            seen_digits.add(happy_number)
            happy_number = sum(int(i) ** 2 for i in str(happy_number))

        return happy_number == 1

