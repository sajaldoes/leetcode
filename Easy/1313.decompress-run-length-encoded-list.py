'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-08 12:07:05
LastEditTime: 2022-09-08 12:13:41
'''
#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []        
        for i in range(0, len(nums), 2):
            ans.extend([nums[i+1]] * nums[i]) #It's better
            # ans+= [nums[i+1]] * nums[i]
        
        return ans

        
# @lc code=end

