"""
2. 尾部的零
设计一个算法，计算出n阶乘中尾部零的个数

您在真实的面试中是否遇到过这个题？
样例
样例  1:
	输入: 11
	输出: 2

	样例解释:
	11! = 39916800, 结尾的0有2个。

样例 2:
	输入:  5
	输出: 1

	样例解释:
	5! = 120， 结尾的0有1个。

挑战 O(logN)的时间复杂度

链接: https://www.lintcode.com/problem/trailing-zeros/description
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        count = 0
        temp = n // 5
        while temp != 0:
            count += temp
            temp //= 5
        return count

s = Solution()
print(s.trailingZeros(12345678987654321))