class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in  range(len(s)):

            if s[i] in s_map:
                s_map[s[i]].append(i)
            else:
                s_map[s[i]] = [i]

            if t[i] in t_map:
                t_map[t[i]].append(i)
            else:
                t_map[t[i]] = [i]

            if s_map[s[i]] != t_map[t[i]]:
                return False

        return True