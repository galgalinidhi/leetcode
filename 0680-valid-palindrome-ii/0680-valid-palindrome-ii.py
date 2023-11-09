class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0 
        p2 = len(s)-1
        
        def ispallindrome(l, r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1     
            return True
        
        while p1<=p2:
            if s[p1]!= s[p2]:
                
                return ispallindrome(p1+1, p2) or ispallindrome(p1, p2-1)
                   
                
            p1+=1
            p2-=1    
        return True
                   
               
                