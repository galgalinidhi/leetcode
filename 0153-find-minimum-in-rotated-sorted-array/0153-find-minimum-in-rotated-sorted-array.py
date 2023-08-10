class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
       
        mini = nums[0]
        while(l<=r):
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                break
            
            m = l+r//2
            if nums[m] >= nums[l]:
                mini = min(mini, nums[l])
                l+=1
            else:
                mini = min(mini, nums[m])
                r-=1
        return mini