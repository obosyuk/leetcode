class Solution:
    def hIndex(self, citations: List[int]) -> int:

        idx_dict = dict()

        def add_to_dict(d: dict, key: int, value: int):
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]

        max_h_index = len(citations)
        for c_idx, val in enumerate(citations):
            if val >= max_h_index:
                add_to_dict(idx_dict, max_h_index, val)
            else:
                add_to_dict(idx_dict, val, val)

        accumulated = 0
        for i in range(len(citations), -1, -1):
            accumulated += len(idx_dict.get(i)) if idx_dict.get(i) else 0
            if accumulated >= i:
                return i

