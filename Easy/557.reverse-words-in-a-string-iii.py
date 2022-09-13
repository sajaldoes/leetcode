'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-13 11:05:51
LastEditTime: 2022-09-13 11:12:44
'''
#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for i in s.split(' '):
            ans.append(i[::-1])
            
        return (" ").join(ans)
        
# @lc code=end

