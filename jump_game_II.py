class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest_jump = 0
        end_position = nums[0]
        jumps = 0

        for idx, el in enumerate(nums):
            if idx == 0:
                continue

            if idx + el >= farthest_jump:
                farthest_jump = idx + el

            if idx == end_position:
                jumps += 1
                end_position = farthest_jump
            else:
                if idx == len(nums) - 1:
                    jumps += 1
                    end_position = farthest_jump

        return jumps
