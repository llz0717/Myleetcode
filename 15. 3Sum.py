class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        
        for i in range(len(nums)):
            if (nums[i]>0):
                break
            elif i==0 or nums[i-1]!=nums[i]:
                left, right = i+1,len(nums)-1
                while left<right:
                    if nums[left]+nums[right]<-nums[i]:
                        left+=1
                    elif nums[left]+nums[right]>-nums[i]:
                        right-=1
                    else:
                        answer.append((nums[i],nums[left],nums[right]))
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left +=1                
                             
        return answer
