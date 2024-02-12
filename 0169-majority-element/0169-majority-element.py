class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
            
        for k,v in freq.items():
            if freq[k] > len(nums)//2:
                return k