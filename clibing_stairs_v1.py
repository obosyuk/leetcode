# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0,1):
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)