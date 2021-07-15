class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        stack = [[T[0], 0]]

        for i in range(1, len(T)):
            while stack and stack[-1][0] < T[i]:
                val = stack.pop()
                ret[val[1]] = i - val[1]
            stack.append([T[i], i])

        print(ret)
        return ret


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        stack = []

        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret