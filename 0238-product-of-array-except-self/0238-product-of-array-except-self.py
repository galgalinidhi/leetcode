class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        ans=[1]*(len(nums))
        for i in range(0,len(nums)):
            ans[i]=pre
            pre*=nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=post
            post*= nums[j]
      
        return ans    