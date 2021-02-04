"""
667. 优美的排列 II
给定两个整数n和k，你需要实现一个数组，这个数组包含从1到n的 n个不同整数，同时满足以下条件：

① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组[|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有k 个不同整数；.

② 如果存在多种答案，你只需实现并返回其中任意一种.

示例 1:

输入: n = 3, k = 1
输出: [1, 2, 3]
解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1


示例 2:

输入: n = 3, k = 2
输出: [1, 3, 2]
解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2


提示:

n和k满足条件1 <= k < n <= 104.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-arrangement-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from comm import func_time


class Solution:
    @func_time
    def constructArray(self, n: int, k: int) -> List[int]:
        nnn = list(range(1, n + 1))

        if k == 1:
            return nnn

        i, j = 0, k
        for kk in range(k, 0, -2):
            i_value = nnn[i] + kk
            nnn.remove(i_value)
            i += 1
            nnn.insert(i, i_value)
            i += 1

        return nnn

    @func_time
    def constructArray2(self, n: int, k: int) -> List[int]:

        ans = []
        for i in range(int(k / 2 + 1)):
            ans.append(i + n - k)
            if i + n - k - 1 < n - i - 1:
                ans.append(n - i)
        b = list(range(1, n - k))
        return b + ans


if __name__ == '__main__':
    n = 100
    k = 10
    S = Solution()
    print(S.constructArray(n, k))
    print(S.constructArray2(n, k))
