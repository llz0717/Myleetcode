class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minvalue=10**4
        
        
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            t2=target-nums[i]
            
            while j<k:
                if abs(nums[j]+nums[k]-t2)<minvalue:
                    minvalue=abs(nums[j]+nums[k]-t2)
                    ans=nums[i]+nums[j]+nums[k]
                
                if nums[j]+nums[k]<t2:
                    j+=1
                elif nums[j]+nums[k]>=t2:
                    k-=1
        
        return ans
