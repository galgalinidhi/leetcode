class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        left = 0
        right = n
        top = 0
        bottom = n
        matrix = [[0 for _ in range(n)]for _ in range(n) ]
        ele = 1
        while left<right and top<bottom:
            
            #fill the top row
            for i in range(left,right):
                matrix[top][i] = ele
                ele+=1
            top+=1
            
            
            #fill the right row
            for i in range(top, bottom):
                matrix[i][right-1] = ele
                ele+=1
            right-=1
            
            #fill the bottom row
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i] = ele
                ele+=1
            bottom-=1
            
            #fill the left row
            for i in range(bottom-1,top-1,-1):
                matrix[i][left] = ele
                ele+=1
            left+=1    
        return matrix        