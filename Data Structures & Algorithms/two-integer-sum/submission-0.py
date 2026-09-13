class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i, a in enumerate(nums):
            b = target - a
            if storage.get(b) is not None:
                return [storage.get(b), i]
            storage[a] = i
        return []