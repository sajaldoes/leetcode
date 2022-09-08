'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-08 12:15:43
LastEditTime: 2022-09-08 12:31:55
'''
#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(s)

        #Learned <3
        for i, c in enumerate(s):
            ans[indices[i]] = c
        
        return "".join(ans)
# @lc code=end

