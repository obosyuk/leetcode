class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_list = list(str(x))
        if len(x_list) % 2 == 0:  # ['1', '2', '3', '4']
            return x_list[:len(x_list) / 2] == list(reversed(x_list[len(x_list) // 2:]))
        else:  # ['1', '2', '3']
            return x_list[:len(x_list) // 2] == list(reversed(x_list[len(x_list) // 2 + 1:]))
        return False