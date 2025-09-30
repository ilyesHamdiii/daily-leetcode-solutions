#https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30
# Time:O(n*n)
# 
# # Space:O(n)
class Solution:
    def triangularSum(self, nums):
        l1 = []

        while len(nums) != 1:
            for i in range(len(nums)-1):
                number = (nums[i] + nums[i+1]) % 10
                l1.append(number)
            nums = l1[:]
            l1 = []
        return nums[0]