"""
10.01. 合并排序的数组
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m

链接：https://leetcode-cn.com/problems/sorted-merge-lcci
"""
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        A.sort()
        print(A)

    def merge2(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        双指针

        复杂度分析
        时间复杂度：O(m+n)O(m+n)
        指针移动单调递增，最多移动 m+nm+n 次，因此时间复杂度为 O(m+n)O(m+n)。

        空间复杂度：O(m+n)O(m+n)
        需要建立长度为 m+nm+n 的中间数组 sorted。

        """
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] < B[pb]:
                sorted.append(A[pa])
                pa += 1
            else:
                sorted.append(B[pb])
                pb += 1
        A[:] = sorted

    def merge3(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        逆向双指针
        时间复杂度：O(m+n)O(m+n)
        指针移动单调递减，最多移动 m+nm+n 次，因此时间复杂度为 O(m+n)O(m+n)。

        空间复杂度：O(1)O(1)
        直接对数组 A 原地修改，不需要额外空间。

        :return:
        """
        pa, pb = m - 1, n - 1
        tail = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1


s = Solution()
A = [1, 2, 3, 0, 0, 0]
m = 3
B = [2, 5, 6]
n = 3
# [1,2,2,3,5,6]
s.merge(A, m, B, n)
s.merge2(A, m, B, n)
s.merge3(A, m, B, n)
