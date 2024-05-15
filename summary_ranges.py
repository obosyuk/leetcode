class Solution:
    def rangeToStr(self, range_: List[int]) -> str:
        return f"{range_[0]}" if range_[0] == range_[1] else f"{range_[0]}->{range_[1]}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [f"{nums[0]}"]

        list_of_ranges = []

        range_ = [nums[0], nums[0]]
        for idx, num in enumerate(nums[1:]):
            if num == range_[1] + 1:
                range_[1] = num
            else:
                list_of_ranges.append(self.rangeToStr(range_))
                range_ = [num, num]

            if idx == len(nums) - 2:
                list_of_ranges.append(self.rangeToStr(range_))

        return list_of_ranges


