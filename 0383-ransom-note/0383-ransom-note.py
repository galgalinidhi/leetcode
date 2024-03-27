class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
   
        for i in range(len(magazine)):
            hashmap[magazine[i]] = 1 + hashmap.get(magazine[i],0)
            
        for j in range(len(ransomNote)):
            if hashmap.get(ransomNote[j], 0) == 0:
                return False
            hashmap[ransomNote[j]] -=1
        return True    