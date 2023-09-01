class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        numset = set()
        
        for end in range(len(s)):
            while s[end] in numset:
                numset.remove(s[start])
                start+=1
            numset.add(s[end])
            res = max(res, (end-start)+1 )
        return res
        
        