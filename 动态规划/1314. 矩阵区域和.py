"""
1314. 矩阵区域和
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

链接：https://leetcode-cn.com/problems/matrix-block-sum
"""
import time
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        answer = []

        for i, m_1 in enumerate(mat):
            n = len(m_1)
            res = []
            for j, m_2 in enumerate(m_1):
                # i - K <= r <= i + K, j - K <= c <= j + K 
                ans = 0
                for r in range(max(0, i - K), min(i + K + 1, m)):

                    for c in range(max(0, j - K), min(j + K + 1, n)):
                        ans += mat[r][c]
                res.append(ans)
            answer.append(res)
        return answer

    def matrixBlockSum2(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
        官方题解思路
            https://leetcode-cn.com/problems/matrix-block-sum/solution/ju-zhen-qu-yu-he-by-leetcode-solution/
        :param mat:
        :param K:
        :return:
        """
        # 二维前缀和问题
        m, n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i][j - 1] + presum[i - 1][j] - presum[i - 1][j - 1] + mat[i - 1][j - 1]

        res = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                x0 = max(0, i - K)
                x1 = min(i + K + 1, m)
                y0 = max(0, j - K)
                y1 = min(j + K + 1, n)
                res[i][j] = presum[x1][y1] - presum[x1][y0] - presum[x0][y1] + presum[x0][y0]
        return res


s = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
K = 1
print(s.matrixBlockSum(mat, K))
print(s.matrixBlockSum2(mat, K))
