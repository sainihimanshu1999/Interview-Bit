class Solution:
    def merge(self, intervals, new_interval):
        if new_interval.start > new_interval.end:
            new_interval.start , new_interval.end = new_interval.end , new_interval.start

        result = []
        newStart = new_interval.start
        newEnd = new_interval.end

        i = 0
        while i<len(intervals) and new_interval.start>intervals[i].end:
            result.append(intervals[i])
            i += 1
        
        while i<len(intervals) and new_interval.end >= intervals[i].start:
            newStart = min(new_interval.start, intervals[i].start)
            newEnd = max(new_interval.end, intervals[i].end)
            i += 1
        result.append(Interval(newStart,newEnd))

        while i<len(intervals):
            result.append(intervals[i])
            i+=1

        return result
        
