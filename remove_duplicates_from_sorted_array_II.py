class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates_dict = dict()
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            if num in duplicates_dict:
                if duplicates_dict[num] < 2:
                    duplicates_dict[num] += 1
                    idx += 1
                else:
                    del nums[idx]
            else:
                duplicates_dict[num] = 1
                idx += 1