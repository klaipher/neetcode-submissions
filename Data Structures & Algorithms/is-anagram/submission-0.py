class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter1, counter2 = {}, {}
        for s1, s2 in zip(s, t):
            counter1[s1] = 1 + counter1.get(s1, 0)
            counter2[s2] = 1 + counter2.get(s2, 0)
        return counter1 == counter2