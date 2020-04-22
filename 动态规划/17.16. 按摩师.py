"""
面试题 17.16. 按摩师
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动



示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12

链接: https://leetcode-cn.com/problems/the-masseuse-lcci/
"""
import random
from typing import List
from copy import deepcopy


class Solution:

    def massage(self, nums: List[int]) -> int:
        """
        自己解法
        :param nums:
        :return:
        """
        if not nums:
            return 0

        len_nums = len(nums)
        dp = deepcopy(nums)
        for i in range(2, len_nums):
            for j in range(i - 1):
                dp[i] = max(dp[i], nums[i] + dp[j])

        return max(dp)

    def massage2(self, nums: List[int]) -> int:
        """
        更快解法
        状态转移方程为：f(n)=max( f(n-2)+nums[n], f(n-1) )
        f(n)指的是数组前n项的最大值。因为题目中要求不能取相邻的值，那么计算f(n)时就可分为两种情况：
        1、取到了当前值，即nums[n]，此时就不能再取与其相邻的前一个值 nums[n-1]，那么最后得到的f(n)只能是f(n-2)与nums[n]的和；
        2、未取到当前值，那就意味着可以取到前一个值nums[n-1]，此时的f(n)就等于f(n-1)。最后，选择这两种情况下的最大值即可作为f(n)的最终结果。
        :param nums:
        :return:
        """

        a, b = 0, 0
        for x in nums:
            b, a = max(a + x, b), b
        return b

    def massage3(self, nums: List[int]) -> int:
        """
        官方解法, 二维数组
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return 0
        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)  # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]  # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1

        return max(dp0, dp1)


s = Solution()
# n = [1, 2, 3, 1]
# n = [2, 7, 9, 3, 1]
# n = [2, 1, 4, 5, 3, 1, 1, 3]
# n = []
n = list(range(10))
random.shuffle(n)
print(n)
print(s.massage(n))
print(s.massage2(n))
print(s.massage3(n))
