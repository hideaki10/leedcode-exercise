#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x)

        while a != 0:
            temp = a % 10
            num = num * 10 + temp
            a = a//10

        if x < 0 and num <= 2 ** 31:
            return -num
        elif x > 0 and num < 2 ** 31 - 1:
            return num
        else:
            return 0
# @lc code=end
