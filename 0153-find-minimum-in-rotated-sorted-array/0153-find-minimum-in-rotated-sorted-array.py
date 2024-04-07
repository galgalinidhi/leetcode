class Solution:
    def findMin(self, nums: List[int]) -> int:
      
        
        def binarysearch(l,r):
            while(l<=r):
                mid = (l+r)//2
                if nums[mid]<nums[mid-1]:
                    return nums[mid]
                elif nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                elif nums[mid]>nums[0]:
                    l= mid+1
                else:
                    r = mid-1
            
          
        if len(nums) ==1 or nums[0]<nums[-1]:
            return nums[0]
        else:
            l = 0
            r = len(nums)-1
            return(binarysearch(l,r))        