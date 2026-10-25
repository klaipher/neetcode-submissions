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

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        _, pivot = self.binary_search(-1, n - 1, lambda i: nums[i] <= nums[-1])
        real = lambda i: (i + pivot) % n
        bad, good = self.binary_search(-1, n, lambda i: nums[real(i)] >= target)
        if good < n and nums[real(good)] == target:
            return real(good)
        return -1