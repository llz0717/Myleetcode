# use + two add two string together
class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]!='-':
            ans=x[::-1]
        else:
            ans='-'+x[-1:-len(x):-1]
            # ans=-int(ans)
        
        ans=int(ans)
        
        if -2**31<=ans and ans<=2**31 -1:
            return ans
        else:
            return 0
