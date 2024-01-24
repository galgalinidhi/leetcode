class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 1
        
        while (left<right) and right<len(nums):
            
            if nums[left]!=nums[right]:
                left = right
                right = right+1
            
            else:
                return nums[left]
            