class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        maxlen = 1
        for i in range(len(s)):
            l=i
            r=i
            res = ""
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
            if len(res)>=maxlen:
                maxlen = len(res)
                final = res
        
        for i in range(len(s)):
            l = i
            r = l+1
            res = ""
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
            if len(res) >maxlen:
                maxlen = len(res)
                final = res
        return final