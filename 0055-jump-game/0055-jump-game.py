class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        curr = target - 1
        
        if len(nums) == 1:
            return True
        while curr>=0:
                               
            if curr + nums[curr] >= target:
                target-=1
                curr = target -1
                
            else:
                curr-=1
                if curr<0:
                    return False
                
        return True
            
        