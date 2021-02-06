class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        count = 0
        while i < 32:
            val = 1 << i
            if n & val == val:
                count += 1
            i += 1
        return count