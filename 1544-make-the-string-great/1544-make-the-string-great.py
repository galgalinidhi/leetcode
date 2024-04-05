class Solution:
    def makeGood(self, s: str) -> str:
        
        def great(res:str):
            
            l = 0 
            r = l+1
           
            while l<r and r<len(res):
                if abs(ord(res[l])-ord(res[r])) == 32:
                    if r+1<len(res):
                        res = res[0:l]+res[r+1:]
                    else:    
                        res = res[0:l]  
                      
                    return great(res)
                
                else:
                    l +=1
                    r = l+1
                    
            return res   
                    
        return great(s)        