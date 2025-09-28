class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res = {}
        total = 0
        # For all values in given list
        for num in nums:
            # Determine if we have seen the value before
            if num in res.keys():
                res[num] = res.get(num) + 1
            else:
                res[num] = 1
        # Get the highest frequency
        maxfreq = max(res.values())
        # Get all the vlues that have that frequency there are a couple ways to approach this but since we have to look through them any ways I just add it to total
        for vals in res.values(): 
            if vals == maxfreq:
                total += vals
        return total