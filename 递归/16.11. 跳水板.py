"""
16.11. 跳水板

你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：

0 < shorter <= longer
0 <= k <= 100000

链接：https://leetcode-cn.com/problems/diving-board-lcci
"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:

        if k == 0:
            return []

        if shorter == longer:
            return [k * shorter]

        res = [0] * (k + 1)
        for i in range(k + 1):
            res[i] = (k - i) * shorter + i * longer
        return res

        # return list(range(shorter * k, longer * k + 1, longer - shorter))

s = Solution()
shorter = 1
longer = 1
k = 10000
print(s.divingBoard(shorter, longer, k))
