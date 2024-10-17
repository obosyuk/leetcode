class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        longest_sequences = []
        longest_sequence = []

        for el in nums:
            if len(longest_sequence) > 0 and longest_sequence[-1] == el-1:
                longest_sequence.append(el)
            else:
                if len(longest_sequence) > 0:
                    longest_sequences.append(longest_sequence)
                longest_sequence = [el]

        longest_sequences.append(longest_sequence)

        longest_sequence = []
        for sequence in longest_sequences:
            if len(sequence) > len(longest_sequence):
                longest_sequence = sequence
        return len(longest_sequence)



