# find minimum in rotated sorted array
Problem:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
Solution: 
https://github.com/ayun01/algorithm/blob/master/find-minimum-in-rotated-sorted-array.py

1. 不会有倒序这种情况。比如：7654321
2. 所以，一共可以有3种情况。如图。
![rotated sorted array](https://user-images.githubusercontent.com/33712067/34464620-346b3f1c-ee3c-11e7-8a65-8e22aba11c18.PNG)
3. 使target为nums[length-1]，然后找第一个element使得element <= target。如果是case1，target为最大的元素，显然满足条件，如果是case2或3，那么target就是中间的某个元素。找第一个小于它的，就是找最小元素。
4. 判断mid和target的大小。如果mid<=target，应该往左找，如case1和case3。否则，往右找，如case2。
