class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hashset1 = {}
        hashset2 = {}
        c = 0 
        for w in words1:
            hashset1[w] = 1+ hashset1.get(w,0)
        for w in words2:
            hashset2[w] = 1+hashset2.get(w,0)
        
      
        for k,v in hashset2.items():
            if hashset2[k] == 1 and hashset1.get(k,0) == 1:
                c+=1
            
            
        return c    
    
            