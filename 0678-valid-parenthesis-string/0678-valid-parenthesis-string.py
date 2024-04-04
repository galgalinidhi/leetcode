class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if stack !=[] and s[stack[-1]] == '(':
                    stack.pop()
                elif star!=[]:
                    star.pop()
                else:
                    return False
        while stack != [] and star!= []:
            if stack[-1] >star[-1]:
                return False
            stack.pop()
            star.pop()
        if stack == []:
            return True   
                
            