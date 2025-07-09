class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]] #1st interval insterted to avoid a edge case

        for start, end in intervals[1:]: #skipped 1st interval as we added it to o/p above
            lastEnd = output[-1][1] #this is edge case mentioned in 4th line
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output