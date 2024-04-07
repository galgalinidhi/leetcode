class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        def binarysearch(l,r):
          
            while(l<=r):
                m = (l+r)//2
                if nums[m] == target:
                    return m
                if target>nums[m]:
                    l = m+1
                else:
                    r = m-1
            return -1
        
        for i in range(len(nums)):
           
            if i+1<len(nums) and nums[i]>=nums[i+1]:
                pivot = i+1
                break
            else:
                pivot = len(nums)
        
      
        if binarysearch(0,pivot-1) !=-1:
            return binarysearch(0,i)
        else:
            return binarysearch(pivot, len(nums)-1)
        
           
     
         