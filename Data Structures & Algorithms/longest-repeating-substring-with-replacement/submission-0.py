from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        best = 0
        cnt = defaultdict(int)
        max_freq = 0
        for end, current_symb in enumerate(s):
            cnt[current_symb] += 1
            max_freq = max(max_freq, cnt[current_symb])
            if end - start + 1 - max_freq > k:
                cnt[s[start]] -= 1
                start += 1
            best = max(best, end - start +1)
        return best