#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2025-10-27
# Time:O(n)
# Medium
# Space:O(n)


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        prev=0
        for row in bank:
            dev=row.count('1')
            if dev>0:
                ans+=dev*prev
                prev=dev
        return ans