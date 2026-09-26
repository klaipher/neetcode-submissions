class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n- k
        window_sum = sum(cardPoints[:window_size])
        best = total - window_sum
        start = 0
        for end in range(window_size, n):
            window_sum += cardPoints[end]
            window_sum -= cardPoints[start]
            start += 1
            best = max(best, total - window_sum)
        return best
