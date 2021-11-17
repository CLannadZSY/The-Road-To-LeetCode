/*

318. 最大单词长度乘积
给定一个字符串数组words，找到length(word[i]) * length(word[j])的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。



示例1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。


提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i]仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
]*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	words := []string{"abcw", "baz", "foo", "bar", "xtfn", "abcdef"}
	fmt.Println(maxProduct(words))
}

// 笨比如我, 不咋会位运算
func maxProduct(words []string) int {
	maxRes := 0
	i, j := 0, 1
	l := len(words) - 1
	wordLen := make(map[int]int)
	for i, v := range words {
		wordLen[i] = len(v)
	}

	for i < l {

		if !strings.ContainsAny(words[i], words[j]) {
			maxRes = max(maxRes, wordLen[i]*wordLen[j])
		}

		if j == l {
			i++
			j = i
		}

		j++

	}

	return maxRes
}

func max(x, y int) int {
	if x > y {
		return x
	}

	return y
}
