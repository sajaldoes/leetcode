'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-03 09:58:20
LastEditTime: 2022-09-03 10:06:45
'''
#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans
        
# @lc code=end

