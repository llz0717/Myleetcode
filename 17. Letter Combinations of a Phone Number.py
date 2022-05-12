class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        if not digits:
            return []
        res =[c for c in dic[digits[0]]]
        
        for d in digits[1::]:
            res=[i+c for i in res for c in dic[d]]
        
        return res
