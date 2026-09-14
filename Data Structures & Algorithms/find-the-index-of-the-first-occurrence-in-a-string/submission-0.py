class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if len(needle) == j:
                    return i - j
                    break
            else:
                i = i - j + 1
                j = 0
        else:
            return -1