# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1

        start_idx = 0
        end_idx = len(nums) - 1

        while start_idx < end_idx:
            mid_idx = (start_idx + end_idx) // 2

            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] > target:
                end_idx = mid_idx - 1 if mid_idx > 0 else 0
            elif nums[mid_idx] < target:
                start_idx = mid_idx + 1

        if nums[end_idx] < target:
            return end_idx + 1
        else:
            return end_idx

