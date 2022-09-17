'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-13 11:40:52
LastEditTime: 2022-09-17 10:59:07
'''
#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n%2==0:
            return [i for i in range(-(n//2),n//2+1) if i!=0]
        else:
            return [i for i in range(-(n//2),n//2+1)]
# @lc code=end

