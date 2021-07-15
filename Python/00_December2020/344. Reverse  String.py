class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ln = len(s)
        for i in range(int(ln / 2)):
            tmp = s[i]
            s[i] = s[ln - 1 - i]
            s[ln - 1 - i] = tmp


    def reverseStringTwoPointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # 결과적으로 로직은 같으나 나눗셈을 하지 않는다. (2번째것이 더 빠름

    def reverseStringSimpleRev(self, s: List[str]) -> None:
        s.reverse() # 두번째 빠름

    def reverseStringListComp(self, s: List[str]) -> None:
        s[:] = s[::-1] # 가장 빠름