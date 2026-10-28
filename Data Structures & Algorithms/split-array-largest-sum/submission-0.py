class Solution:
    def can_finish(self, limit):
        worker = 1
        current_sum = 0
        for num in self.nums:
            if current_sum + num > limit:
                worker += 1
                current_sum = 0
            current_sum += num
        return worker <= self.k

    def binary_search(self, bad, good):
        while good - bad > 1:
            mid = (bad + good) // 2
            if self.can_finish(mid):
                good = mid
            else:
                bad = mid
        return bad, good

    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        bad, good = self.binary_search(max(nums) - 1, sum(nums))
        return good


