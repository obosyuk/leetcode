# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        threshold = len(nums) / 2

        for el in nums:
            if el in nums_dict:
                nums_dict[el] += 1
            else:
                nums_dict[el] = 1

            if nums_dict[el] > threshold:
                return el

