"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

链接：https://leetcode-cn.com/problems/range-sum-query-immutable
"""
from typing import List


class NumArray:
    """
    15/16
    20万个次计算, 超出时间限制
    原因分析:
        1. self._dp 字典中不是保存每个下表元素的和, 而是应该保存前 N 项的和, 这样直接使用减法就能直接算出结果
        而不需要使用for循环, 每个元素都去判断于取值
        2. 你怎么知道这个前N项一定被计算过, 且保存了结果到 self._dp 字典中?
        3. 还是说, 在类初始化, 就计算N项和保存到self._dp字典中, 后面所有的取值, 都只需要执行第一步即可??
        4. 第三种方法似乎可行
    """

    def __init__(self, nums: List[int]):
        self._nums = nums

    def sumRange(self, i: int, j: int) -> int:
        self._dp = dict()
        _list_len = len(self._nums)

        def sum_index(self, m, n):
            res = 0
            for x in range(m, min((n + 1), _list_len)):
                if x in self._dp:
                    res += self._dp[x]

                if isinstance(self._nums[x], list):
                    self._dp[x] = sum_list(self._nums[x])
                else:
                    self._dp[x] = self._nums[x]

                res += self._dp[x]

            return res

        def sum_list(n):

            if n and isinstance(n[0], list):
                return sum_list(n[0])
            else:
                return sum(n)

        return sum_index(self, i, j)


class NumArray2:
    """
    可以计算多维列表的求和, 官方给出的是一维列表的求和
    """
    def __init__(self, nums: List[int]):
        self._nums = nums
        self._dp = dict()

    def sumRange(self, i: int, j: int) -> int:

        if (i and j) in self._dp:
            if i <= 0:
                return self._dp[j]
            return self._dp[j] - self._dp[max(i - 1, 0)]

        # self._dp 的下标 key 代表前 N 项和
        for m, x in enumerate(self._nums):

            # 应该保存前 N 项和, 而不是第 N 个
            sum_res = x

            if x and isinstance(x, list):
                sum_res = sum_list(x)

            if m == 0:
                self._dp[m] = sum_res
                continue

            self._dp[m] = self._dp[m - 1] + sum_res

        if i <= 0:
            return self._dp[j]

        return self._dp[j] - self._dp[max(i - 1, 0)]

    def __del__(self):
        print(self._dp)


def sum_list(n):
    if n and isinstance(n[0], list):
        return sum_list(n[0])
    else:
        return sum(n)


class NumArray3:
    """
    一维 官方解法
    """
    def __init__(self, nums: List[int]):
        length = len(nums)
        self.total = [0] * (length + 1)
        for i in range(length):
            self.total[i + 1] = self.total[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.total[j + 1] - self.total[i]


if __name__ == '__main__':
    # nums = [[[[[[]]]]]]
    # 列表: [-2, 0, 3, -5, 2, -1], 下标: [0, 2], [2, 5], [0, 5]等
    # nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    nums = [-2, 0, 3, -5, 2, -1]

    # obj = NumArray2(nums)
    #
    # x, y = 1, 2
    # param_1 = obj.sumRange(x, y)
    # print(param_1)
    # x, y = 0, 3
    # param_1 = obj.sumRange(x, y)
    # print(param_1)

    obj = NumArray3(nums)

    x, y = 1, 2
    param_1 = obj.sumRange(x, y)
    print(param_1)
    x, y = 0, 3
    param_1 = obj.sumRange(x, y)
    print(param_1)
