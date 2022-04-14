# good example: pick one number, search its left and right to check Palindromic
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxlength=0
        maxstring=[]
        
        for i in range(len(s)):
            # odd string
            l,r=i,i            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>maxlength:
                    maxstring=s[l:r+1]
                    maxlength=r-l+1
                l-=1
                r+=1
            
            # even string
            l,r=i,i+1           
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>maxlength:
                    maxstring=s[l:r+1]
                    maxlength=r-l+1
                l-=1
                r+=1           
                
        return maxstring
        
