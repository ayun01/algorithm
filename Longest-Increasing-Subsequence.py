# Given a sequence of integers, find the longest increasing subsequence (LIS).
# You code should return the length of the LIS.
# For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
# For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4
# https://leetcode.com/problems/longest-increasing-subsequence/description/

# n^2 
# dp[i]: from 0 to i, longest increasing subsequence
# dp[i] = max(dp[i],dp[j] + 1}, initial dp[i] = 1, j = 0:i-1 and A[j] < A[i].
# 
# nlogn
# 可以参考：
# (1) https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# (2) http://blog.csdn.net/dangwenliang/article/details/5728363/
# 
# 九章的算法合并了(1)中的case 1 和case 3，它们都可以看做是replace。因为binarysearch返回的是右边界，所以在case1中，如果A[i]<=minLast中的任何一个，那么它replace的就是A[1]. 同理在case3中，它会replace第一个>=A[i]的数。
# 在case2中，因为minLast已经被初始化为都是maxint，除了minLast[0]。所以找到的index就是minLast的结尾(最后一个被replace/append的地方).
# case 1: 如果A[i] <= minLast[0], replace minLast[0] with A[i]。
# case 2: 如果A[i] > minLast[len],len是当前最大长度。
# case 3: 如果A[i] 在minLast[0]到minLast[len]之间，binarysearch找到第一个>=A[i]的数，然后replace it with A[i]。

# n^2
class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # dp[i]: from 1 to i LIS
        # parameter check
        if nums is None or len(nums) == 0:
            return 0
            
        n = len(nums)
        dp = [1 for i in xrange(n)]
        
        for i in xrange(1,n):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        
        return max(dp)

# nlogn
import sys
class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or len(nums) == 0:
            return 0
            
        MIN_INT = -(sys.maxint + 1)
        tail = [nums[0]]
        length = 1
        for i in xrange(1,len(nums)):
            #print tail,nums[i]
            if nums[i] <= tail[0]:
                tail[0] = nums[i]
            elif nums[i] > tail[-1]:
                tail.append(nums[i])
                length += 1
            else:
                index = self.binarySearch(tail, nums[i])
                #print 'index=',index,tail[index],nums[i]
                tail[index] = nums[i]
                
        #print tail
        return length

    
    def binarySearch(self,tail,target):
        l,r = 0, len(tail) - 1
        while l + 1 < r:
            m = l + (r-l)/2
            if target > tail[m]:
                l = m
            else:
                r = m
        
        # return the first elem that >= target
        return r
