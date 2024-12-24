class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        k = 0
        p1, p2 = 0, len(nums) - 1
        while p1 <= p2:
            if nums[p1] == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
                k += 1

        return k
