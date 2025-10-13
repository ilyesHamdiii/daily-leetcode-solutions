#https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13
# Time:O(n)
# Easy
# Space:O(n)
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        cur = []
        for word in words:
            if cur == sorted(word):
                continue
            else:
                ans.append(word)
                cur = sorted(word)
        return ans

        