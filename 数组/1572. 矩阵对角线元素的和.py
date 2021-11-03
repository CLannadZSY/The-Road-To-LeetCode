"""
1572. 矩阵对角线元素的和
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。



示例 1：



输入：mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
示例 2：

输入：mat = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]
输出：8
示例 3：

输入：mat = [[5]]
输出：5


提示：

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-diagonal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    # 笨比如我
    def diagonalSum(self, mat: List[List[int]]) -> int:
        h = len(mat)
        w = len(mat[0])
        res = dict()

        i, j = 0, 0
        while i < h and j < w:
            res[(i, j,)] = mat[i][j]
            i += 1
            j += 1

        i, j = h - 1, 0
        while i >= 0 and j < w:
            res[(i, j,)] = mat[i][j]
            i -= 1
            j += 1

        return sum(res.values())

    def diagonalSum2(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            ans += mat[i][i] + mat[i][len(mat) - 1 - i]
        if len(mat) % 2:
            ans -= mat[len(mat) // 2][len(mat) // 2]
        return ans