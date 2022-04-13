from numpy import *
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans=full((n,n),0)
        # ans=[[0]*n for _ in range(n)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        currx=curry=currd=0
        
        for i in range(1,n*n+1):
            ans[currx][curry]=i
            
            newx,newy=currx+direction[currd][0], curry+direction[currd][1]
            
            if newx<0 or newx>=n or newy<0 or newy>=n or ans[newx][newy]:
                currd=(currd+1)%4
            currx+=direction[currd][0]
            curry+=direction[currd][1]
        
        return ans
