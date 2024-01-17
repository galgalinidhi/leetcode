class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []
        answer =[[], []]
        for i in range(len(matches)):
            winners.append(matches[i][0]) 
            losers.append(matches[i][1])
        winners = sorted(set(winners))
       
        
        freq = {}
        for i in range(len(losers)):
            freq[losers[i]] = 1 + freq.get(losers[i],0)
     
        for i in range(len(winners)):
            if freq.get(winners[i],0) == 0:
                answer[0].append(winners[i])
         
          
        for k,v in freq.items():
            
            if freq[k] == 1:
               
                answer[1].append(k)
        answer[1].sort()
        return answer