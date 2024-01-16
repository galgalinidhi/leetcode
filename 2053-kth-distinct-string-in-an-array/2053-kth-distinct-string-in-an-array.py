class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq ={}
        res = []
        for i in range(len(arr)):
            freq[arr[i]] = 1+ freq.get(arr[i],0)
        
        for i in range(len(arr)):
            if freq[arr[i]] == 1:
                res.append(arr[i])
        
        if len(res)<k:
            return ""
        return res[k-1]