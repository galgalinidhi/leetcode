class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(1,len(nums)):
            left=[]
            right =[]
            left = nums[0:i]
            right = nums[i+1:len(nums)]
            
            if sum(left) == sum(right):
                return i-1
        return -1