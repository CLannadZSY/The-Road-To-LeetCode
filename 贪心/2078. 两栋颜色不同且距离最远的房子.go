/*
2078. 两栋颜色不同且距离最远的房子

街上有 n 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 0 开始且长度为 n 的整数数组 colors ，其中 colors[i] 表示第 i 栋房子的颜色。

返回 两栋 颜色 不同 房子之间的 最大 距离。

第 i 栋房子和第 j 栋房子之间的距离是 abs(i - j) ，其中 abs(x) 是 x 的绝对值。

示例 1：

输入：colors = [1,1,1,6,1,1,1]
输出：3
解释：上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
注意，房子 3 和房子 6 也可以产生最佳答案。
示例 2：



输入：colors = [1,8,3,8,3]
输出：4
解释：上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。
示例 3：

输入：colors = [0,1]
输出：1
解释：两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。


提示：

n ==colors.length
2 <= n <= 100
0 <= colors[i] <= 100
生成的测试数据满足 至少 存在 2 栋颜色不同的房子

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

package main

import "fmt"

func main() {
	colors := []int{0, 1}
	fmt.Println(maxDistance(colors))

}

func maxDistance(colors []int) int {
	l := len(colors)
	i, j := 0, l-1

	maxRes := 0
	for i < l-1 {
		if colors[i] != colors[j] {
			maxRes = max(maxRes, j-i)
		}
		j--
		if j == i {
			j = l - 1
			i++
		}
	}
	return maxRes
}

//贪心算法
//作者：endlesscheng
//链接：https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors/solution/on-zuo-fa-by-endlesscheng-an8b/
func maxDistance2(colors []int) (ans int) {
	n := len(colors)
	c := colors[0]
	if c != colors[n-1] {
		return n - 1
	}
	l, r := 1, n-2
	for colors[l] == c {
		l++
	}
	for colors[r] == c {
		r--
	}
	return max(r, n-1-l)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
