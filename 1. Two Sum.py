class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # method 1: one point, best
        # empty map    
        mapping={}
        for i in range(len(nums)):
            ans=target-nums[j]            
            # if there is answer in current map, return answer
            # else keep build mapping
            if ans in mapping and mapping[ans]!=j:
                return [j,mapping[ans]] 
            
            mapping[nums[i]]=i
            
        # methond2, two point
        # two loop, not necessary
        mapping={}
        for i in range(len(nums)):
            mapping[nums[i]]=i
                    
        for j in range(len(nums)):
            ans=target-nums[j]
            if ans in mapping and mapping[ans]!=j:
                return [j,mapping[ans]]    
        
