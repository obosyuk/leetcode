# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for el in nums:
            if el in nums_dict:
                nums_dict[el] += 1
            else:
                nums_dict[el] = 1

        for key, value in nums_dict.items():
            if value > len(nums) / 2:
                return key
