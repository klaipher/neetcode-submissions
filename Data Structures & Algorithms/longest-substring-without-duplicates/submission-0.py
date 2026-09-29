from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        best = 0
        cnt = defaultdict(int)
        for end, current_symb in enumerate(s):
            cnt[current_symb] += 1
            while cnt[current_symb] > 1:
                cnt[s[start]] -= 1
                start += 1
            best = max(best, end - start +1)
        return best