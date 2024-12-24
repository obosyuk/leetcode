class Solution:
    def convert(self, s: str, numRows: int) -> str:

        str_list = ["" for _ in range(numRows)]

        pointer = 0  # 0 ... len(s) - 1
        str_idx = 0  # 0 ... numRows - 1
        forward = True

        while pointer <= len(s) - 1:
            str_list[str_idx] += s[pointer]
            pointer += 1
            if forward:
                if str_idx < numRows - 1:
                    str_idx += 1
                else:
                    str_idx -= 1
                    forward = False
            else:
                if str_idx > 0:
                    str_idx -= 1
                else:
                    str_idx += 1
                    forward = True

        return "".join(str_list)


