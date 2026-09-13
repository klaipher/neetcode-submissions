class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1
            if counter[num] > 1:
                return True
        return False