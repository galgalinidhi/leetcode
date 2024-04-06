class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_index = []
        res = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack!=[] and i>stack[-1]:
                    #match
                    stack.pop()
                else:
                    remove_index.append(i)
      
        while stack!=[]:
            
            remove_index.append(stack.pop())
       
        for i in range(len(s)):
            if i in remove_index:
                continue
            res+= s[i]    
        return res    
        
        
                    
                