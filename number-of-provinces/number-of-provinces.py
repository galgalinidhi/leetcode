class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:    
        obj = S(len(isConnected))
        c = 0 
        for i in range(0,len(isConnected)):
            for j in range(0,len(isConnected[0])):    
                if i!=j and isConnected[i][j] == 1:
                    obj.union(i,j)
        for i in range(len(isConnected)):
            if i == obj.find(i):
                c+=1
        return c        

    
class S:  
      
        # parent = []
        # rank = []
        def __init__(self, n):
            self.parent = [i for i in range(n)]         
            self.rank = [1] * n
        
        def find(self,x):
            if x == self.parent[x]:
                return x
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self,x,y):
            x_val = self.find(x)
            y_val = self.find(y)
        
            if x_val!=y_val:
                if self.rank[x_val]> self.rank[y_val]:
                    self.parent[y_val] = x_val
                elif self.rank[y_val]>self.rank[x_val]:
                    self.parent[x_val] = y_val
                else:
                    self.parent[y_val] = x_val
                    self.rank[x_val]+=1
        
        
        