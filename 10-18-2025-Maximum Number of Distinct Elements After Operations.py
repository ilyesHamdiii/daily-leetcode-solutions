#https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/?envType=daily-question&envId=2025-10-18
# Time:O(n)
# Medium
# Space:O(n)



class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        distinct_num = set()
        nums[0] = nums[0] - k
        distinct_num.add(nums[0])
        for i in range(1, len(nums)):
            wanted_num = nums[i - 1] + 1
            if abs(nums[i] - wanted_num) <= k:
                nums[i] = wanted_num
            else:
                nums[i] = max(nums[i] - k, nums[i - 1])
            
            distinct_num.add(nums[i])

        return len(distinct_num)