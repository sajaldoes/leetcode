#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i]
            digits[i] = (digits[i]+carry) % 10
            carry = (temp+carry)//10

        if carry==0: return digits
        else: return [1] + digits

        
# @lc code=end

