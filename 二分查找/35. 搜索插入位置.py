"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

链接：https://leetcode-cn.com/problems/search-insert-position
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """双指针"""
        if target in nums:
            return nums.index(target)

        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] < target:
                i += 1
            else:
                return i

            if nums[j] > target:
                j -= 1
            else:
                return j

        return i

    def searchInsert2(self, nums: List[int], target: int) -> int:
        """二分查找"""
        n = len(nums)
        left, right = 0, n - 1
        ans = n
        while left <= right:
            mid = (right - left) // 2 + left
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

    def searchInsert3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


s = Solution()
nums = [1, 3]
target = 2
print(s.searchInsert(nums, target))
print(s.searchInsert2(nums, target))
print(s.searchInsert3(nums, target))
