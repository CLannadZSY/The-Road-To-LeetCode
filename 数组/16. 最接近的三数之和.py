"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

链接：https://leetcode-cn.com/problems/3sum-closest
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closeNum = nums[0] + nums[1] + nums[2]
        for i, m in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[l] + m + nums[r]
                # print(nums[l], m, nums[r], threeSum)
                if abs(closeNum - target) > abs(threeSum - target):
                    closeNum = threeSum
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return target
        return closeNum


s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))
