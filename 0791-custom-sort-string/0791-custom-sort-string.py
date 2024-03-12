class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        res = []
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
        
        for i in range(len(order)):
            if freq.get(order[i],0) !=0:
                while freq[order[i]]!=0:
                    res.append(order[i])
                    freq[order[i]]-=1
                    
        res = ''.join(res)
        for k,v in freq.items():
            if freq[k]!=0:
                res+=k*v
        
        return res