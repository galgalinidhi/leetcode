class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1 for i in range(len(nums))]
        right_prod = [1 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]
        prefix = 1
        suffix = 1
       
        for i in range(1,len(nums)):
            prefix*= nums[i-1]
            left_prod[i] = prefix
        for  j in range(len(nums)-2,-1,-1):
            suffix*= nums[j+1]
            right_prod[j] = suffix
                
        for i in range(len(nums)):
            res[i]= res[i]*left_prod[i]*right_prod[i]
        return res    
        