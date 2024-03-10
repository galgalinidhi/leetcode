class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        res = 0
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
         
        sort_freq = dict(sorted(freq.items(), key = operator.itemgetter(1), reverse = True))
       
        
        for k, v in sort_freq.items():
            if freq[k]>=max_freq:
                max_freq = freq[k]
                res+=freq[k]
        
        return res