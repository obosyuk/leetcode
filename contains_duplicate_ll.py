class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nums_dict = dict()
        for idx, num in enumerate(nums):
            if num in nums_dict:
                for d_idx in nums_dict[num]:
                    if abs(d_idx - idx) <= k:
                        return True

                nums_dict[num].append(idx)

            else:
                nums_dict[num] = [idx]

        return False

