#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if a+b == target and i != j:
                    return [i, j]

# @lc code=end
