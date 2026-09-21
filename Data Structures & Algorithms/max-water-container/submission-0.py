class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        best_area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                right -= 1
                left += 1
            current_area = min(height[left], height[right]) * (right - left)
            best_area = max(current_area, best_area)
        return best_area