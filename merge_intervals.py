class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])

        new_intervals = []
        prev_interval = []

        for interval in intervals:
            if not prev_interval:
                prev_interval = interval
            else:
                if prev_interval[1] >= interval[0]:
                    # if prev_interval[1] >= interval[1]:
                    if interval[1] >= prev_interval[1]:
                        prev_interval[1] = interval[1]
                else:
                    new_intervals.append(prev_interval)
                    prev_interval = interval

        # new_intervals.append(prev_interval)
        # if new_intervals and new_intervals[-1][1] <=  prev_interval[0] and prev_interval[1] > new_intervals[-1][1]:
        #     new_intervals.append(prev_interval)
        if new_intervals and prev_interval[1] < new_intervals[-1][1]:
            return new_intervals
        new_intervals.append(prev_interval)
        return new_intervals

