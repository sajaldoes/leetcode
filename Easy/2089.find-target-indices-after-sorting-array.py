'''
Author: Sajal Das [@sajaldoes]
Date: 2022-09-13 11:18:43
LastEditTime: 2022-09-13 11:38:21
'''
#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # nums = sorted(nums)
        # return [i for i in range(len(nums)) if nums[i]==target]
        #Learned from Discussion
        index = 0
        count = 0
        for n in nums:
            if n < target:
                index+=1
            if n == target:
                count+=1
            
        return list(range(index, index+count))


        
# @lc code=end

