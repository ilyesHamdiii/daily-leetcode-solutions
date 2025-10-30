#https://leetcode.com/problems/make-array-elements-equal-to-zero/description/?envType=daily-question&envId=2025-10-28
# Time:O(n)
# Easy
# Space:O(n)
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix, cnt=0, 0
        Sum=sum(nums)
        for x in nums:
            prefix+=x
            if x==0:
                cnt+=2*(2*prefix==Sum)
                cnt+=(abs(2*prefix-Sum)==1)
        return cnt