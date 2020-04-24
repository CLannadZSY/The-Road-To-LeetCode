"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5
 
限制：
0 <= 数组长度 <= 50000

链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
"""
import random
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        超时, 意料之中
        :param nums:
        :return:
        """

        res = 0
        for i, n in enumerate(nums):

            for j in range(i + 1, len(nums)):

                if n > nums[j]:
                    res += 1

        return res

    def reversePairs2(self, nums: List[int]) -> int:
        """
        记录下标位置和大小, 然后进行判断, 如果这样, 那就直接将结果进行累加, 但是判断条件应该怎么写呢

        :param nums:
        :return:
        """

        res = 0
        len_nums = len(nums)
        # 如果存在重复元素, 就会有下标计算问题
        sort_nums = sorted(nums)






s = Solution()
nums = [7, 5, 6, 4]
nums = list(range(10))
random.shuffle(nums)
print(nums)
print(s.reversePairs(nums))
print(s.reversePairs2(nums))
