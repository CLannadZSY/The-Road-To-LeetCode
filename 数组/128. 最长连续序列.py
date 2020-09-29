"""
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为O(n)。

示例:

输入:[100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
"""
from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        个人, 但是好像有点慢
        :param nums:
        :return:
        """
        set_nums = set(nums)
        count = 1
        ret = 0

        for n in nums:
            current_num = n
            next_n = current_num + 1
            while next_n in set_nums:
                count += 1
                current_num = next_n
                next_n = current_num + 1

            ret = max(ret, count)
            count = 1
        return ret

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        官方题解
        :param nums:
        :return:
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
# nums = [0]
# nums = [0, 0]
# nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 34, 5, 5, 6, 6, 7, 7, 89, 9, 0]
print(s.longestConsecutive(nums))
print(s.longestConsecutive2(nums))
