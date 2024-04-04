class Solution:
    def isValid(self, s: str) -> bool:
        start = '{(['
        stack = []
        d = {'}':'{', ')':'(', ']':'['}
        for each in s:
            if each in start:
                stack.append(each)
            else:
                if stack != [] and stack[-1] == d[each]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

                
                