# if I use for loop, it exceeds runnint time
# while  is much better 
class Solution:
    def intToRoman(self, num: int) -> str:
        # running time is a problem
        ans=''        
        while num>=1000:
                num=num-1000
                ans=ans+'M'
        while num>=900:
                num=num-900
                ans=ans+'CM'
        while num>=500 :
                num=num-500
                ans=ans+'D'                
        while num>=400:
                num=num-400
                ans=ans+'CD'
        while num>=100:
                num=num-100
                ans=ans+'C'
        while num>=90:
                num=num-90
                ans=ans+'XC'
        while num>=50:
                num=num-50
                ans=ans+'L'
        while num>=40:
                num=num-40
                ans=ans+'XL'
        while num>=10:
                num=num-10
                ans=ans+'X'
        while num>=9:
                num=num-9
                ans=ans+'IX'
        while num>=5:
                num=num-5
                ans=ans+'V'
        while num>=4:
                num=num-4
                ans=ans+'IV'
        while num>=1:
                num=num-1
                ans=ans+'I'
        
        return ans
