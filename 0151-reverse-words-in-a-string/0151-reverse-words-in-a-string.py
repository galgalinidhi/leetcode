class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        res = ""
        for i in range(len(lst)-1, -1, -1):
            
                res+= lst[i]
                if i-1>=0:
                    res+= " "
        return res            