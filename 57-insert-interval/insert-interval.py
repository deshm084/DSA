class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval
        i, n = 0, len(intervals)

        # add all intervals completely before newInterval
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # merge overlaps
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1

        # add merged interval
        res.append([s, e])

        # add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res





               