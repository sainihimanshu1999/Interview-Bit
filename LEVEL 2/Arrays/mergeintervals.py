def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1].end<intervals[i].start:
                res.append(intervals[i])
            elif res[-1].end>intervals[i].end:
                continue
            else:
                res[-1].end = intervals[i].end
        return res