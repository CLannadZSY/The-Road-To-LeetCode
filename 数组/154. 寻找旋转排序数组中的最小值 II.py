"""
154. 寻找旋转排序数组中的最小值 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
"""
from typing import List

"""双指针"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """二分法"""
        min_num = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            min_num = min(min_num, nums[left], nums[right])
            left += 1
            right -= 1

        return min_num

    def findMin2(self, nums: List[int]) -> int:
        """二分查找"""
        low = 0
        high = len(nums) - 1
        while high > low:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]


s = Solution()
nums = [2, 2, 2, 0, 1]
print(s.findMin(nums))
print(s.findMin2(nums))
