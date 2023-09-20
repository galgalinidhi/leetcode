class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i=0
        
        intervals.sort(key = lambda i: i[0])
       
        for i in range(len(intervals)):
            
            if not res or res[-1][1]< intervals[i][0]:
                res.append(intervals[i])
            elif res[-1][1]>=intervals[i][0]:
                merge = res.pop()
                m = [min(merge[0], intervals[i][0]),
                         max(merge[1], intervals[i][1])]
                res.append(m)
        return res
        # while i < len(intervals):
        #     if intervals[i+1]:
        #         if intervals[i+1][0]<=intervals[i][1]:
        #             merge = [min(intervals[i+1][0], intervals[i][0]),
        #                 max(intervals[i+1][1], intervals[i][1])]
        #             res.append(merge)
        #             i+=2
        #         else:    
        #             res.append(intervals[i])
        #             i+=1
        # return res
            