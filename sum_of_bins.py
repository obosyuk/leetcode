class Solution:
    def getItemFromList(self, lst: list[int], index: int) -> int:
        try:
            return lst[index]
        except:
            return 0

    def addBinary(self, a: str, b: str) -> str:
        l1 = list(reversed(list(map(int, a))))
        l2 = list(reversed(list(map(int, b))))

        shift_to_next = False
        sum_of_bins = []

        iter_len = max(len(l1), len(l2))

        for i in range(iter_len):
            s = self.getItemFromList(l1, i) + self.getItemFromList(l2, i)
            if shift_to_next is True:
                s += 1

            if s == 2:
                sum_of_bins.append(0)
                shift_to_next = True
            elif s == 3:
                sum_of_bins.append(1)
                shift_to_next = True
            else:
                sum_of_bins.append(s)
                shift_to_next = False

        if shift_to_next:
            sum_of_bins.append(1)

        return "".join(str(x) for x in reversed(sum_of_bins))
