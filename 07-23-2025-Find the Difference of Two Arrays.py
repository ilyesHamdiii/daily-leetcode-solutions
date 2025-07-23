# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy


# Time: O(n)
# Space: O(n)
class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1Set=set(nums1)
        nums2Set=set(nums2)
        res1=set()
        res2=set()
        for n in nums1:
            if n not in nums2Set:
                res1.add(n)
        for n in nums2:
            if n not in nums1Set:
                res2.add(n)
        return [list(res1),list(res2)]