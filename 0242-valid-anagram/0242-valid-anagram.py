class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        
        if len(s) != len(t):
            return False
        for i in range(0,len(s)):
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)
            
        if freq_s == freq_t:
            return True
        return False