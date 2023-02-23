class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s =""
        for ch in s:
            if ch.isalnum():
                alnum_s+=ch
                alnum_s+=ch
        alnum_s= alnum_s.lower()
        lptr = 0
        rptr = len(alnum_s)-1
        while lptr<=rptr:
           
            if alnum_s[lptr] != alnum_s[rptr]:
                return False
            lptr+=1
            rptr-=1
        return True
                
            