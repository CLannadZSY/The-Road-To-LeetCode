/*
62. 圆圈中最后剩下的数字
0,1,,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4 这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6

链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
*/
package main

import "fmt"

func lastRemaining(n int, m int) int {
    f := 0
    for i := 2; i < n + 1; i++ {
        f = (f + m) % i
    }
    return f
}

func main() {
    n, m := 5, 3
    fmt.Println(lastRemaining(n, m))
}