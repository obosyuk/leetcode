class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates_dict = {}

        p1 = 0

        while p1 <= len(nums) - 1:
            if nums[p1] in duplicates_dict:
                del nums[p1]
                continue
            else:
                duplicates_dict[nums[p1]] = None
                p1 += 1

        return len(nums)