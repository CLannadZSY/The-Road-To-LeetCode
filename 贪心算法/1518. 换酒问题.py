"""
1518. 换酒问题
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。

链接：https://leetcode-cn.com/problems/water-bottles
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles

        while numBottles >= numExchange:
            empty_bottles = numBottles % numExchange
            numBottles //= numExchange
            drink += numBottles

            numBottles += empty_bottles

        return drink