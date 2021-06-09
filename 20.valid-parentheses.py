#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            # stack　后进先出 会取出最后进来也就是前面一个
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        # 只有右边的括号的时候，会滞留stack里，不会pop出来，所以不等于0 会返回False
        return len(stack) == 0
# @lc code=end
