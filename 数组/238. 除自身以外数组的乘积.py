"""
238. 除自身以外数组的乘积
给你一个长度为n的整数数组nums，其中n > 1，返回输出数组output，其中 output[i]等于nums中除nums[i]之外其余各元素的乘积。



示例:

输入: [1,2,3,4]
输出: [24,12,8,6]


提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

链接：https://leetcode-cn.com/problems/product-of-array-except-self
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        """
        双指针
        :param nums:
        :return:
        """
        left, right = 1, 1
        res = [1] * len(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums):
            res[i] *= left
            res[j] *= right
            left *= nums[i]
            right *= nums[j]

            i += 1
            j -= 1

        return res


s = Solution()
nums = [1, 2, 3, 4]
# 前 N 项和
# [1, 1, 2, 6]
print(s.productExceptSelf(nums))  # [24,12,8,6]
print(s.productExceptSelf2(nums))  # [24,12,8,6]
