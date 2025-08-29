class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, end = 0, 0  # track best palindrome indices

        def expand(l: int, r: int) -> None:
            nonlocal start, end
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # After expanding, l and r are one step beyond palindrome
            if r - l - 1 > end - start:
                start, end = l + 1, r - 1

        for i in range(len(s)):
            expand(i, i)       # odd length palindrome
            expand(i, i + 1)   # even length palindrome

        return s[start:end + 1]
