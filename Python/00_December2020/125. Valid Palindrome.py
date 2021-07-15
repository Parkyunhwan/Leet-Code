# 유효한 팰린드롬 (회문)
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = []
        for c in s:
            if c.isalnum():
                if c.isalpha():
                    c = c.lower()
                li.append(c)

        for i in range(int(len(li) / 2)):
            if li[i] != li[len(li) - 1 - i]:
                return False
        return True


    def isPalindromeBySlicingAndRE(self, s: str) -> bool:
        s = s.lower()
        # 정규식을 통한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]