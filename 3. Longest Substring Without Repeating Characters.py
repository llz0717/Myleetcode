class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        norepeatstring=[]
        maxlength=0
        
        for i in s:
            if i in norepeatstring:
                index=norepeatstring.index(i)
                del norepeatstring[0:index+1]
                norepeatstring.append(i)
            else:    
                norepeatstring.append(i)
                if maxlength<len(norepeatstring):                   
                    maxlength=len(norepeatstring)
        
        return maxlength
 

# harshmap is also very good
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans      
      
