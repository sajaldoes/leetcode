'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-03 10:16:42
LastEditTime: 2022-09-04 16:11:18
'''
#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    cnt+=1
        
        return cnt
        
# @lc code=end

