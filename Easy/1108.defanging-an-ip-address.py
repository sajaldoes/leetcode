'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-03 10:08:53
LastEditTime: 2022-09-03 10:12:34
'''
#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
            if i==".":
                ans+="[.]"
            else:
                ans+=i
        
        return ans
        
# @lc code=end

