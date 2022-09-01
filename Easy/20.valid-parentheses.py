#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        braces = {')':'(','}':'{',']':'['}

        for i in s:
            if i in braces.values():
                stack.append(i)
            elif stack and stack[-1]==braces[i]:
                stack.pop()
            else:
                return False
            
        return True if not stack else False
            
            

# @lc code=end

