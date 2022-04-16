class Solution:
    def maxArea(self, height: List[int]) -> int:
        
     #   if len(height)<3:
     #       maxwater=(min(height[0],height[1]))  * 1
     #   else:
        
            left,right=0,len(height)-1

            maxwater=(min(height[left],height[right]))  * (right-left)

            while left<right:
                currentwater=(min(height[left],height[right])) * (right-left)
                
                
                if currentwater>=maxwater:
                        maxwater=currentwater
                
                if height[left]>=height[right]:
                    right-=1
                elif height[left]<height[right]:
                    left+=1
                


        
        return maxwater
