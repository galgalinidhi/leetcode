class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq ={}
        n = len(nums)
        for i in range(0,n):
            if nums[i] not in  freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        for i in range(0,n):
            if freq[nums[i]]> n//2:
                return nums[i]
        