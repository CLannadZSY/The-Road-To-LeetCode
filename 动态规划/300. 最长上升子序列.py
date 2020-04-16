"""
300. 最长上升子序列(https://leetcode-cn.com/problems/longest-increasing-subsequence/)

给定一个无序整数数组, 找到其中最长上升子序列的长度

示例:
    输入: [10, 9, 2, 5, 3, 7, 101, 18]
    输出: 4
    解释: 最长的上升子序列是 [2, 3, 7, 101], 它的长度是4

说明:
    1. 可能会有多种最长上升子序列, 你只需要输出对应的长度即可
    2. 你算法的时间负责度应该为 O(n^2)

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

注意「子序列」和「子串」这两个名词的区别，
子串一定是连续的，而子序列不一定是连续的。

"""
import random
from typing import List


def longest_increasing_subsequence(num_list: List[int]) -> int:
    """
    动态规划解法
    :param num_list: 无序整数列表
    :return: 子序列长度
    """
    num_len = len(num_list)
    dp = [1] * num_len
    for i in range(num_len):
        for j in range(i):
            if num_list[i] > num_list[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

def longest_increasing_subsequence_2(num_list: List[int]) -> int:
    """
    动态规划 + 二分查找
    :param num_list: 无序整数列表
    :return: 子序列长度
    """
    tails, res = [0] * len(num_list), 0
    for n in num_list:
        i, j = 0, res
        while i < j:
            m = (i + j) // 2
            if tails[m] < n:
                i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
            else:
                j = m

        tails[i] = n
        if j == res:
            res += 1
    return res


if __name__ == '__main__':
    num = list(range(10))
    random.shuffle(num)
    print(num)
    print(longest_increasing_subsequence(num))
    print(longest_increasing_subsequence_2(num))
























