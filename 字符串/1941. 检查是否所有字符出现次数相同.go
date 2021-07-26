/*
1941. 检查是否所有字符出现次数相同
给你一个字符串 s ，如果 s 是一个 好 字符串，请你返回 true ，否则请返回 false 。

如果 s 中出现过的 所有 字符的出现次数 相同 ，那么我们称字符串 s 是 好 字符串。

 

示例 1：

输入：s = "abacbc"
输出：true
解释：s 中出现过的字符为 'a'，'b' 和 'c' 。s 中所有字符均出现 2 次。
示例 2：

输入：s = "aaabb"
输出：false
解释：s 中出现过的字符为 'a' 和 'b' 。
'a' 出现了 3 次，'b' 出现了 2 次，两者出现次数不同。
 

提示：

1 <= s.length <= 1000
s 只包含小写英文字母。
*/

package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "aaabb"
	fmt.Println(areOccurrencesEqual(s))
}

// 个人解法
func areOccurrencesEqual(s string) bool {
	d := map[int]int{}
	for i := 97; i < 123; i++ {
		d[i] = strings.Count(s, string(i))
	}

	sameCount := 0
	for _, y := range d {
		if y == 0 {
			continue
		} else if sameCount == 0 {
			sameCount = y
		} else if sameCount != y {
			return false
		}
	}

	return true
}

// 另一种思路
func areOccurrencesEqual2(s string) bool {
	time := make(map[int32]int, 0)
	for _, char := range s {
		time[char]++
	}
	t := 0
	for _, v := range time {
		t = v
	}
	for _, v := range time {
		if t != v {
			return false
		}
	}
	return true
}