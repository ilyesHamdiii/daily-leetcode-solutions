#https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Time:O(Nlogn+Mlogn)
# Easy
# # Space:O(n)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        l=[]
        for i in spells:
            if i*potions[-1]<success:
                l.append(0)
                continue
            count=0
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if potions[mid]*i>=success:
                    high=mid-1
                else:
                    low=mid+1
            l.append(n-low)
        return l