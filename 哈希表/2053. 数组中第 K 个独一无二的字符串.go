/*

2053. 数组中第 K 个独一无二的字符串
独一无二的字符串指的是在一个数组中只出现过 一次的字符串。

给你一个字符串数组arr和一个整数k，请你返回arr中第k个独一无二的字符串。如果少于k个独一无二的字符串，那么返回空字符串""。

注意，按照字符串在原数组中的 顺序找到第 k个独一无二字符串。



示例 1:

输入：arr = ["d","b","c","b","c","a"], k = 2
输出："a"
解释：
arr 中独一无二字符串包括 "d" 和 "a"。
"d" 首先出现，所以它是第 1 个独一无二字符串。
"a" 第二个出现，所以它是 2 个独一无二字符串。
由于 k == 2 ，返回 "a" 。
示例 2:

输入：arr = ["aaa","aa","a"], k = 1
输出："aaa"
解释：
arr 中所有字符串都是独一无二的，所以返回第 1 个字符串 "aaa" 。
示例 3：

输入：arr = ["a","b","a"], k = 3
输出：""
解释：
唯一一个独一无二字符串是 "b" 。由于少于 3 个独一无二字符串，我们返回空字符串 "" 。


提示：

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i]只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-distinct-string-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
package main

import "fmt"

func main() {
	arr := []string{"d", "b", "c", "b", "c", "a"}
	k := 2
	fmt.Println(kthDistinct(arr, k))
}

func kthDistinct(arr []string, k int) (ans string) {
	cnt := map[string]int{}
	for _, s := range arr {
		cnt[s]++
	}
	for _, s := range arr {
		if cnt[s] == 1 {
			if k--; k == 0 {
				return s
			}
		}
	}
	return

}