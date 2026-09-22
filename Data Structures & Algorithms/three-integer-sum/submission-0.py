class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # -4, -1, -1, 0, 1, 2
        result = []
        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                if total < 0:
                    second += 1
                elif total > 0:
                    third -= 1
                else:
                    result.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1    
                    second += 1
                    third -= 1
        return result