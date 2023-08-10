class Solution:
    def isPalindrome(self, s: str) -> bool:
        n_str =""
        for ch in s:
            if ch.isalnum():
                n_str += ch.lower()
        
        l = 0
        r = len(n_str)-1
        while (l<=r):
            if n_str[l] == n_str[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True