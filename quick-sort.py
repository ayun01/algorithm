class Solution:
    """
    @param: A: an integer array
    @return: 
    """
    def sortIntegers2(self, A):
        if A is None:
            return None
        
        self.quickSort(A, 0, len(A)-1)
        
    
    def quickSort(self, A , start, end):
        if start >= end:
            return
        
        left,right = start,end
        # 选取start或者last，都容易造成极端值，所以选mid，也可以用random，但这个有cost
        mid = left + (right - left)/2
        pivot = A[mid]
        # 1.left <= right : left 和 right 互相越过，它们之间的差可以为1或者2
        # example [1,2] pivot = 1 then split to [1] and [1,2], 问题的规模没有减小
        while left <= right:
            # 2.不能等于pivot，否则在极端情况下会出现left = -1 和剩下的，或者right = length 和剩下的
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            
            if left <= right:
                A[left],A[right] = A[right],A[left]
                left += 1
                right -=1
        
        self.quickSort(A,start,right)
        self.quickSort(A,left,end)
            
        
