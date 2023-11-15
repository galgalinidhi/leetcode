class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        r = 1
        computeSum = nums[0]
        
        res = nums[0]
        if len(nums) == 1:
            return nums[0]
        while  r<len(nums):
           
           
            computeSum+= nums[r]
            if nums[r] > computeSum:
                
                computeSum = nums[r]
               
            res = max(res, computeSum)
            r+=1             
        return res        
            