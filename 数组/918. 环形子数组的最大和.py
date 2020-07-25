"""
918. 环形子数组的最大和
给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，而当 i >= 0 时 C[i+A.length] = C[i]）

此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

 

示例 1：

输入：[1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3
示例 2：

输入：[5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
示例 3：

输入：[3,-1,2,-1]
输出：4
解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
示例 4：

输入：[3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
示例 5：

输入：[-2,-3,-1]
输出：-1
解释：从子数组 [-1] 得到最大和 -1
 

提示：

-30000 <= A[i] <= 30000
1 <= A.length <= 30000

链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """超出时间限制"""
        ret = max(A)
        l = len(A)
        i, j = 0, l
        B = A
        while i < l:
            while j > i:
                ret = max(ret, sum(B[i: j]))
                j -= 1
            i += 1
            B = A + A[:i]
            j = len(B)

        return ret

    def maxSubarraySumCircular2(self, A: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/huan-xing-zi-shu-zu-de-zui-da-he-by-leetcode/
        Kanade 算法介绍, 大佬们, 膜拜

        """
        ans = cur = None
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        return ans


s = Solution()
A = [5, -3, 5]
print(s.maxSubarraySumCircular(A))
