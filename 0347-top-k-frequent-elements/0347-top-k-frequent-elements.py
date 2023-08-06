class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Bucket = [[] for b in range(0,len(nums)+1)]
        freq={}
        res =[]
        for i in range(0,len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
       
        for v,f in freq.items():
            Bucket[f].append(v)
        for j in range(len(Bucket)-1, 0, -1):
            for ans in Bucket[j]:
                res.append(ans)
                if len(res) == k:
                    return res