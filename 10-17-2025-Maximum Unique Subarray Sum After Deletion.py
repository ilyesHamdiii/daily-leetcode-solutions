#https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-10-17
# Time:O(n)
# Medium
# Space:O(n)


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set(nums)
        newS = set(n for n in s if n>0)
        if len(newS) == 0:
            return max(nums)
        return sum(newS)