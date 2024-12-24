class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_jump = nums[0]
        for idx, num in enumerate(nums):
            if max_jump <= 0 and idx < len(nums) - 1:
                return False

            if num >= max_jump:
                max_jump = num
            else:

                max_jump -= 1
                if max_jump <= 0 and idx < len(nums) - 1:
                    return False

        return max_jump >= 0
