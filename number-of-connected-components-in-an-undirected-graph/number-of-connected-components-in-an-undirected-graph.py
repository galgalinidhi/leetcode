class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [0] * n
        for i in range(0,n):
            parent[i] = i
            
        def find(x):
            return parent[x]
            # while x!= parent[x]:
            #     x = parent[x]
            # return x 
        def union(x,y):
            x_val = find(x)
            y_val = find(y)
            if x_val!=y_val:
                # parent[y_val] = x_val
                for i in range(len(parent)):
                    if parent[i] == y_val:
                        parent[i] = x_val
                
        for i in range(len(edges)):
            x,y = edges[i]
            union(x,y)
        return len(set(parent))    
        
                
            