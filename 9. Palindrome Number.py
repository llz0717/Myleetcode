class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # dont use string 
        # return str(x) == str(x)[::-1]
        
        # find the digit of this number        
        div=1        
        while x>div*10:
            div*=10        
        while x:
            rightdig=x%10
            leftdig=x//div
            
            if rightdig!=leftdig:
                return False
            else:
                x=(x%div)//10
                div/=100
        
        return True
