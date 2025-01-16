class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = dict()
        for idx, a in enumerate(numbers):
            if a in num_dict:
                num_dict[a].append(idx)
            else:
                num_dict[a] = [idx]

        # print(num_dict)

        # num_dict = {a: idx for idx, a in enumerate(numbers)}

        returnned_idxs = []

        for num, idxs in num_dict.items():

            if target - num in num_dict:
                if num != target - num:
                    return sorted([idxs[0] + 1, num_dict[target - num][0] + 1])
                else:
                    return sorted([idxs[0] + 1, num_dict[target - num][1] + 1])