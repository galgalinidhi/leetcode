import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True
        for j in range(len(t)):
            
            if  s[i] == t[j]:
                i+=1
                if i == len(s):
                    return True
                j+=1
            else:
                j+=1
            
        return False    
           
             
       