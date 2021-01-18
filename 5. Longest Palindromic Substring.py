class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkMore(s, left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1][right - 1]

        if len(s) < 2 or s[:] == s[::-1]:
            return s

        ret = ''
        for start in range(len(s)):
            ret1 = checkMore(s, start, start + 1)
            ret2 = checkMore(s, start, start + 2)
            ret = max(ret, ret1, ret2, key=len)
        return ret