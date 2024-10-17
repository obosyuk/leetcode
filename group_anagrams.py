class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for str_ in strs:
            sorted_str = "".join(sorted(str_))

            if sorted_str not in strs_dict:
                strs_dict[sorted_str] = [str_]
            else:
                strs_dict[sorted_str].append(str_)

        return [strs_dict[k] for k in strs_dict]
