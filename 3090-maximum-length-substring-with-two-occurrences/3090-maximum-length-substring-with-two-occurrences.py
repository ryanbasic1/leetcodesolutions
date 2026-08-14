class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26

        left = 0
        ans = 0

        for right in range(len(s)):

            # Add current character
            count[ord(s[right]) - ord('a')] += 1

            # Shrink window if character occurs more than twice
            while count[ord(s[right]) - ord('a')] > 2:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Current window length
            ans = max(ans, right - left + 1)

        return ans