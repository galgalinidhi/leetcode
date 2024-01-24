class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for i in range(0, len(nums)):
            freq[nums[i]] = 1+ freq.get(nums[i],0)
        
        
        for k in range(1,len(nums)+1):
            if freq.get(k,0) == 2:
                res.append(k)
        
        for k in range(1, len(nums)+1):
            if freq.get(k,0) == 0:
                res.append(k)
                
           
                
            
        return res    