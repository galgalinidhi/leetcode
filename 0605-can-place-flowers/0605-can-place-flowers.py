class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed +[0]
        count = 0
        i =1
        while i<len(flowerbed)-1:
            if flowerbed[i] == 0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] =1
                    count+=1
            i+=1
        if n<=count:
            return True
        else:
            return False