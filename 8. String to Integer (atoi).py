# super bad problem description
class Solution:
    def myAtoi(self, s: str) -> int:        
        ans='0'
        signmark=None
        
        for i in s:
            if i==' ' and not signmark:
                continue
            elif i.isdigit():
                if not signmark:
                    signmark=1
                ans+=i
            elif i=='+' and not signmark:
                signmark=1
            elif i=='-' and not signmark:
                signmark=-1
            else:
                break
                
        ans=int(ans)
        if signmark:
            ans=ans*signmark
             
        if ans<-2**31:
            ans=-2**31
        elif ans>2**31-1:
            ans=2**31-1
            
        return ans
