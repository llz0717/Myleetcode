class Solution:
    def isValid(self, s: str) -> bool:             
        mapping={'(':')','[':']','{':'}'}
        stacks=[]
        
        for i in s:
            if i in mapping:
                stacks.append(i)
            elif stacks==[] or mapping[stacks.pop()]!=i:
                return False
        
        return (stacks==[])
