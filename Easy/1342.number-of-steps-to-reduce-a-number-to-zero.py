'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-06 09:59:59
LastEditTime: 2022-09-06 10:13:17
'''
#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num!=0:
            if num%2 == 0:
                num/=2
            else:
                num-=1
            count+=1
        
        return count
# @lc code=end

