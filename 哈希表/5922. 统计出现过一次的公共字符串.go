/*
5922. 统计出现过一次的公共字符串
给你两个字符串数组 words1 和 words2 ，请你返回在两个字符串数组中 都恰好出现一次 的字符串的数目。



示例 1：

输入：words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
输出：2
解释：
- "leetcode" 在两个数组中都恰好出现一次，计入答案。
- "amazing" 在两个数组中都恰好出现一次，计入答案。
- "is" 在两个数组中都出现过，但在 words1 中出现了 2 次，不计入答案。
- "as" 在 words1 中出现了一次，但是在 words2 中没有出现过，不计入答案。
所以，有 2 个字符串在两个数组中都恰好出现了一次。
示例 2：

输入：words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
输出：0
解释：没有字符串在两个数组中都恰好出现一次。
示例 3：

输入：words1 = ["a","ab"], words2 = ["a","a","a","ab"]
输出：1
解释：唯一在两个数组中都出现一次的字符串是 "ab" 。


提示：

1 <= words1.length, words2.length <= 1000
1 <= words1[i].length, words2[j].length <= 30
words1[i] 和words2[j]都只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-common-words-with-one-occurrence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
package main

import (
	"fmt"
)

func main() {
	words2 := []string{"leetcode", "is", "amazing", "as", "is"}
	words1 := []string{"amazing", "leetcode", "is"}
	fmt.Println(countWords(words1, words2))

}

func countWords(words1 []string, words2 []string) int {
	w1 := make(map[string]int)
	w2 := make(map[string]int)

	for _, w := range words1 {
		w1[w]++
	}

	for _, w := range words2 {
		w2[w]++
	}

	res := 0
	for w, c := range w1 {
		if c == 1 && w2[w] == 1{
			res++
		}
	}

	return res
}
