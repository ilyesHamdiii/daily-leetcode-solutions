#https://leetcode.com/problems/largest-perimeter-triangle/?envType=daily-question&envId=2025-09-28
# Time:O(NLogN)
# 
# # Space:O(n)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0