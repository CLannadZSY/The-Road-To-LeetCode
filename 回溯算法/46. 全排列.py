"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

链接：https://leetcode-cn.com/problems/permutations
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = list()

        def backtrack(nums, tmp):
            if not nums:
                return [[]]

            for i in range(len(nums)):
                print((nums[:i] + nums[i + 1:]), tmp + [nums[i]])
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))
