class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        nums1 = nums1 + nums2        
        nums1.sort()       
        if len(nums1)%2 !=0:
            medval= nums1[len(nums1)//2]
        else:
            medval= 0.5*(nums1[len(nums1)//2] +  nums1[len(nums1)//2 -1])
        
        return medval
