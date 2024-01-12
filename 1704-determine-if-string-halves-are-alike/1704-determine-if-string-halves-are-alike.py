class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u'}
       
        def count_vowels(split_s):
            count = 0
            for ch in split_s:
                if ch.lower() in vowels:
                    count+=1
                    
            return count        
            
            
        if count_vowels(s[0:len(s)//2]) == count_vowels(s[len(s)//2:len(s)]):
            return True
        return False
        