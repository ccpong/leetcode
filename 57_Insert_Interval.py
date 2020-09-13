class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #insert and sort
        updated_intervals=intervals+[newInterval]
        updated_intervals.sort(key = lambda x: x[0]) 
        #print(updated_intervals)
        #combine
        def combine(intervals):
            l=len(intervals)
            if l<=1:
                return intervals
            i=1
            while i<len(intervals):
                #check overlap
                if intervals[i][0]<=intervals[i-1][1]:
                    #have overlap
                    new=[min(intervals[i][0],intervals[i-1][0]) , max(intervals[i][1],intervals[i-1][1])]
                    intervals[i-1:i+1]=[new]
                    #print(intervals)
                else: i+=1
            return intervals
        return combine(updated_intervals)