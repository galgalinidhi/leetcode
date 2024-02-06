class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        for i in range(len(s)):
            
            freq[s[i]] = 1 + freq.get(s[i],0)
       
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
            