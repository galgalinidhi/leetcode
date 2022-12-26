class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}
        freqt={}
        if len(s)!=len(t):
            return False
        for i in range (0,len(s)):
            
            freqs[s[i]] = 1 + freqs.get(s[i],0)
            freqt[t[i]] = 1 + freqt.get(t[i],0)
        for ch in s:
            if freqs[ch] != freqt.get(ch,0):
                return False
        return True
                
            
      