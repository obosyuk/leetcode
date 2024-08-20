class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, n in enumerate(nums):
            if n in nums_map:
                nums_map[n].append(idx)
            else:
                nums_map[n] = [idx]

        if target == 0 and target in nums_map and len(nums_map[target]) > 1:
            return nums_map[target]

        for idx, n in enumerate(nums):
            rest_target = target - n

            # If we have 4 and 4 we need to check if we have more than two indices for them
            if rest_target == n:
                if len(nums_map[rest_target]) > 1:
                    return nums_map[rest_target]

            # If we have 3 and 5 we just check appearance of 3
            else:
                if rest_target in nums_map:
                    return [idx, nums_map[rest_target][0]]