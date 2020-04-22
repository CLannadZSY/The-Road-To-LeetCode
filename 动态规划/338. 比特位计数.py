"""
338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

链接：https://leetcode-cn.com/problems/counting-bits
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        bin_one_count = [0]
        for i in range(1, num + 1):
            one_count = bin(i).count('1')
            bin_one_count.append(one_count)
        return bin_one_count

    def countBits2(self, num: int) -> List[int]:
        """
        求余
        :param num:
        :return:
        """
        ret = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                ret.append(ret[i // 2])
            else:
                ret.append(ret[i - 1] + 1)
        return ret

    def countBits3(self, num: int) -> List[int]:
        """
        位运算
        :param num:
        :return:
        """
        a = [0] * (num + 1)
        for i in range(num + 1):
            if i == 0:
                a[i] = 0
            else:
                a[i] = a[(i & (i - 1))] + 1
        return a


s = Solution()
n = 7
print(s.countBits(n))
print(s.countBits2(n))
print(s.countBits3(n))
