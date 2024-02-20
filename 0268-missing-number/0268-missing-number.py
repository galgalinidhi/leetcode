class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
        
        for i in range(len(nums)+1):
            f = freq.get(i,0)
            if f == 0:
                return i
            
            