class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''

        idx = 0
        while True:

            # 1. Get a prefix to check
            if len(strs[0]) >= idx + 1:
                prefix_to_check = strs[0][:idx+1]
            else:
                # common_prefix = prefix_to_check
                return common_prefix

            # 2. Check if all words starts with the prefix
            # If yes, assign the prefix to common_prefix
            # otherwise, return common_prefix
            for word in strs:
                if not word.startswith(prefix_to_check):
                    return common_prefix

            common_prefix = prefix_to_check

            idx += 1

        return common_prefix




