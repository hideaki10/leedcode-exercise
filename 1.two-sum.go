/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		one := target - nums[i]
		if _, ok := m[one]; ok {
			return []int{m[one], i}
		}
		m[nums[i]] = i
	}
	return nil
}

// @lc code=end

