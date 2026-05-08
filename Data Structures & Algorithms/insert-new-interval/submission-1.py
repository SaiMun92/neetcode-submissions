class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start = 0
        end = 1

        # Two conditions for non-overlap
        for i in range(len(intervals)):
            inter = intervals[i]
            if newInterval[end] < inter[start]: # newInterval end < start of the current interval
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[start] > inter[end]:
                res.append(inter)
            # Continuously update newInterval
            else:
                newInterval = [min(newInterval[start], inter[start]), max(newInterval[end], inter[end])]

        # Add something here...
        res.append(newInterval)
        return res

