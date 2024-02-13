class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPallin(s):
            l = 0
            r = len(s)-1
            while l<=r:
                if s[l]!= s[r]:
                    return False
                r-=1
                l+=1
            return True
        
        for w in words:
            if checkPallin(w) == True:
                return w
        
        return ""
            
                    