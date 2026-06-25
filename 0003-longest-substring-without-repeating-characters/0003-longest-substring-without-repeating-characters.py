class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = 0
        p1 = 0
        count = 0

        while p1 < len(s):
            if s[p1] in s[p:p1]:
                while s[p] != s[p1]:
                    p += 1
                p += 1

            count = max(count, p1 - p + 1)
            p1 += 1

        return count