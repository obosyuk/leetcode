class Solution(object):
    def reverse(self, nums: list[int], start_idx: int, end_idx: int) -> None:
        while start_idx < end_idx:
            temp = nums[start_idx]
            nums[start_idx] = nums[end_idx]
            nums[end_idx] = temp
            start_idx += 1
            end_idx -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);