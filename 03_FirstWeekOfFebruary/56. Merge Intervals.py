class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []

        for val in intervals:
            if merged and val[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], val[1])
            else:
                merged.append(val)

        return merged
