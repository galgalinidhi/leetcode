class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ch = 0
        i = len(s) -1
        
        while s[i] == ' ':
            i-=1
            print(i)
        while s[i] != ' ' and i>=0 :
            ch+=1
            i-=1
        
        
        return ch    