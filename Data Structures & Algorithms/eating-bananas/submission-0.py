import math

class Solution:
    def mid(self, bad, good) -> int:
        return (bad + good) // 2

    def binary_search(self, bad, good, p):
        while good - bad > 1:
            mid = self.mid(bad, good)
            if p(mid):
                good = mid
            else:
                bad = mid
        return bad, good
    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_finish(k):
            hours_needed = sum(math.ceil(pile / k) for pile in piles)
            return hours_needed <= h
        
        bad, good = self.binary_search(0, max(piles), can_finish)
        return good
            