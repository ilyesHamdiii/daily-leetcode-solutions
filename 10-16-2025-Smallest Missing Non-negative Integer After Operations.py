#https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/?envType=daily-question&envId=2025-10-16
# Time:O(n)
# Medium
# Space:O(n)


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = [0] * value

        for i in nums:
            idx = ((i % value) + value) % value
            freq[idx] += 1

        min_freq = min(freq)
        min_index = freq.index(min_freq)

        return value * min_freq + min_index