"""
1052. 爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 

示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

提示：

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1

链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """超时"""
        l = len(customers)
        lc = l - X + 1

        ret = 0
        for i in range(lc):
            calm = sum(customers[i: i + X])
            normal = sum([x for x, y in zip(customers[:i] + customers[i + X:], grumpy[:i] + grumpy[i + X:]) if y == 0])
            ret = max(ret, calm + normal)
        return ret

    def maxSatisfied2(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """再度超时, 73/78"""
        c = 0
        l = len(customers)

        d = dict()
        ret = 0
        for i in range(l):
            if grumpy[i] == 0:
                c += customers[i]
            else:
                d[i] = customers[i]

        for i in range(l - X + 1):
            t = 0
            for j in range(X):
                t += d.get(i + j, 0)
            ret = max(t + c, ret)
        return ret

    def maxSatisfied3(self, customers: List[int], grumpy: List[int], X: int) -> int:
        t = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                t += customers[i]
                customers[i] = 0

        n = sum(customers[:X])
        m = n
        for i in range(1, len(customers) - X + 1):
            m = m + customers[i + X - 1] - customers[i - 1]
            n = max(m, n)
        return n + t


s = Solution()
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
customers = [4, 10, 10]
grumpy = [1, 1, 0]
X = 2
print(s.maxSatisfied(customers, grumpy, X))
print(s.maxSatisfied2(customers, grumpy, X))
print(s.maxSatisfied3(customers, grumpy, X))
