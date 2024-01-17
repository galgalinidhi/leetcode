class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        res = []
        for i in range(len(arr)):
            freq[arr[i]] = 1 + freq.get(arr[i], 0)
        
        for k,v in freq.items():
            if v in res:
                return False
            res.append(v)
        return True     
        