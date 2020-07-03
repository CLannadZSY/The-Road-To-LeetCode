"""
209. 长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""
from typing import List


class Solution:
    """
    子元素并不连续
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        双指针, 滑动窗口
        :param s:
        :param nums:
        :return:
        """
        left = 0
        mincount = float('inf')
        cursum = 0

        for right in range(len(nums)):
            cursum += nums[right]

            while cursum >= s:
                mincount = min(mincount, right - left + 1)
                cursum = cursum - nums[left]
                left += 1

        return mincount if mincount != float('inf') else 0


S = Solution()
s = 15
nums = [1,2,3,4,5]
print(S.minSubArrayLen(s, nums))
