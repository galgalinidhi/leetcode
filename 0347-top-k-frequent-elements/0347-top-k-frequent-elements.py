class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= {}
        res=[]
        count = [[] for i in range (0,len(nums)+1)]
        for i in range  (0,len(nums)):
            freq[nums[i]] = 1+ freq.get(nums[i],0)
        for key,val in freq.items():
            count[val].append(key)
        for j in range (len(count)-1,0,-1):
            for n in count[j]:
                res.append(n)
                if len(res)==k:
                    return res
            