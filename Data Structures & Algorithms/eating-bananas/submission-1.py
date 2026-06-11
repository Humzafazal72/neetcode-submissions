class Solution:
    def time_calc(elf, piles, curr):
        import math
        piles= [math.ceil(pile/curr) for pile in piles]
        return sum(piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end = 1, max(piles)

        last_mid = None
        while start<=end:
            mid = start +(end-start)//2
            if self.time_calc(piles, mid) <= h:
                last_mid = mid
                end = mid-1
            else:
                start = mid+1
        
        return last_mid