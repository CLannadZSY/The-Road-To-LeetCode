"""
1742. 盒子中小球的最大数量

你在一家生产小球的玩具厂工作，有 n 个小球，编号从 lowLimit 开始，到 highLimit 结束（包括 lowLimit 和highLimit ，即n == highLimit - lowLimit + 1）。另有无限数量的盒子，编号从 1 到 infinity 。

你的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 321 的小球应当放入编号 3 + 2 + 1 = 6 的盒子，而编号 10 的小球应当放入编号 1 + 0 = 1 的盒子。

给你两个整数 lowLimit 和 highLimit ，返回放有最多小球的盒子中的小球数量。如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。



示例 1：

输入：lowLimit = 1, highLimit = 10
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：2 1 1 1 1 1 1 1 1 0  0  ...
编号 1 的盒子放有最多小球，小球数量为 2 。
示例 2：

输入：lowLimit = 5, highLimit = 15
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：1 1 1 1 2 2 1 1 1 0  0  ...
编号 5 和 6 的盒子放有最多小球，每个盒子中的小球数量都是 2 。
示例 3：

输入：lowLimit = 19, highLimit = 28
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 12 ...
小球数量：0 1 1 1 1 1 1 1 1 2  0  0  ...
编号 10 的盒子放有最多小球，小球数量为 2 。


提示：

1 <= lowLimit <= highLimit <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from comm import func_time


class Solution:

    @func_time
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        range_f = range(lowLimit, highLimit + 1)
        box_dic = {x: 0 for x in range(1, highLimit + 1)}
        for x in range_f:
            n = x
            if x > 9:
                n = sum(int(m) for m in list(str(x)))
            box_dic[n] += 1

        return max(box_dic.values())

    @func_time
    def countBalls2(self, lowLimit: int, highLimit: int) -> int:

        hash_value = [0] * 46  # 记录某位数和的数字总数
        hash_num = [0] * (highLimit + 1)  # 记录位数之和
        for i in range(1, highLimit + 1):
            hash_num[i] = hash_num[i // 10] + i % 10
        for i in range(lowLimit, highLimit + 1):
            hash_value[hash_num[i]] += 1
        return max(hash_value)

    @func_time
    def countBalls3(self, lowLimit: int, highLimit: int) -> int:

        hash_value = [0] * 46
        tmp = sum(int(j) for j in str(lowLimit))
        hash_value[tmp] += 1
        for i in range(lowLimit + 1, highLimit + 1):
            if not i % 10:
                if i % 100 != 0:
                    tmp -= 8
                else:
                    tmp = sum(int(j) for j in str(i))
            else:
                tmp += 1
            hash_value[tmp] += 1
        return max(hash_value)


if __name__ == '__main__':
    S = Solution()
    low = 1
    hig = 100000
    print(S.countBalls(low, hig))
    print(S.countBalls2(low, hig))
    print(S.countBalls3(low, hig))
