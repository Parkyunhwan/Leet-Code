class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort(reverse=True)
        result = 0
        for greed in g:
            while s and greed > s[-1]:
                s.pop()
            if not s:
                return result
            result += 1
            s.pop()
        return result
