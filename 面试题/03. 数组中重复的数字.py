"""
03. 数组中重复的数字

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
如果不存在, 则返回 -1

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = dict()

        for n in nums:
            if d.get(n):
                return n
            else:
                d[n] = 1

        return -1

s = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
print(s.findRepeatNumber(nums))