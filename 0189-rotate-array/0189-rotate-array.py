class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == len(nums) and k == 0:
            return nums
        right = nums[len(nums)-k:]
    
        for i in range((len(nums)-k-1),-1,-1):
            nums[i+k] = nums[i]
        
        for i in range(len(nums)-k,len(nums)):
            nums[(i+k) % len(nums)] = right[(i+k) % len(nums)]
            
            
       
      
        