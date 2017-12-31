class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if nums is None or len(nums) <= 0:
            return -1
        
        l,r = 0, len(nums) - 1
        
        target = nums[r]
        
        while l + 1 < r:
            m = l + (r-l)/2
            # find the first elem that <= target
            if target >= nums[m]:
                r = m
            else:
                l = m
        
        if nums[l] <= nums[r]:
            return nums[l]
        else:
            return nums[r]
            
