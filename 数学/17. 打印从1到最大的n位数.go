/*
面试题17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]


说明：

用返回一个整数列表来代替打印
n 为正整数

链接: https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
*/

import "math"

func printNumbers(n int) []int {
    var ret = []int{}
    for i := 1; i < int(math.Pow10(n)); i++ {
        ret = append(ret, i)
    }
    return ret
}

func printNumbers2(n int) []int {
    ll := int(math.Pow(10, float64(n)))
    arr := make([]int, ll-1)
    for i :=1; i < ll; i++ {
        arr[i-1] = i
    }

    return arr
}