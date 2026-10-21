class Solution:
    def mid(self, bad: int, good: int) -> int:
        return (bad + good) // 2
     
    def binary_search(self, bad: int, good: int, p: Callable) -> int:
        while good - bad > 1:
            mid = self.mid(bad, good)
            if p(mid):
                good = mid
            else:
                bad = mid
        return bad, good 

    def search(self, nums: List[int], target: int) -> int:
        bad, good = self.binary_search(-1, len(nums), lambda i: nums[i] >= target)
        if good < len(nums) and nums[good] == target:
            return good
        else:
            return -1