class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ""
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = 1+ freq.get(s[i],0)
        one_count = freq["1"]
        if freq["1"]>=1:
            freq["1"]-=1
            
            while freq["1"]!=0:
                res+="1"
                freq["1"]-=1
        for j in range(0,len(s)-one_count):
            res+="0"
        
        
        res+="1"
        return res
            