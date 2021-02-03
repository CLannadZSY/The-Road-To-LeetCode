"""
1732. 找到最高海拔
有一个自行车手打算进行一场公路骑行，这条路线总共由n + 1个不同海拔的点组成。自行车手从海拔为 0的点0开始骑行。

给你一个长度为 n的整数数组gain，其中 gain[i]是点 i和点 i + 1的 净海拔高度差（0 <= i < n）。请你返回 最高点的海拔 。



示例 1：

输入：gain = [-5,1,5,0,-7]
输出：1
解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。
示例 2：

输入：gain = [-4,-3,-2,-1,4,3,2]
输出：0
解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。


提示：

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-highest-altitude
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from comm import func_time


class Solution:

    @func_time
    def largestAltitude(self, gain: List[int]) -> int:
        return max([sum(gain[:i]) for i in range(1, len(gain) + 1)] + [0])


if __name__ == '__main__':
    S = Solution()
    gain = list(range(1, 10000))
    print(S.largestAltitude(gain))
