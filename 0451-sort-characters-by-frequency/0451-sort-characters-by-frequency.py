class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        res = ""
        for i in range(len(s)):
            freq[s[i]] = 1+ freq.get(s[i],0)
         
        sorted_dict = dict(sorted(freq.items(), key = operator.itemgetter(1), reverse = True))
            
        for k,v in sorted_dict.items():
            res+= k*v
        
        return res