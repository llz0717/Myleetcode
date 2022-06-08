class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
                
        def kSum(nums,target,k):
            res=[]
            
            if not nums:
                return res
            
            average=target//k
            if average<nums[0] or average>nums[-1]:
                return res
            
            if k==2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i==0 or nums[i-1]!=nums[i]:
                    for subset in kSum(nums[i+1::],target-nums[i],k-1):
                        res.append([nums[i]]+subset)
            return res
            
            
        def twoSum(nums,target):
            ans=[]
            l,r=0,len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target or (l>0 and nums[l-1]==nums[l]):
                    l+=1
                elif nums[l]+nums[r]>target or (r<len(nums)-1 and nums[r+1]==nums[r]):
                    r-=1
                else:
                    ans.append([nums[l],nums[r]])
                    l+=1
                    r-=1
                    
            return ans
            
        nums.sort()
        return kSum(nums,target,4)
