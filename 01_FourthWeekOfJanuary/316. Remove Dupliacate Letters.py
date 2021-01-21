# 중복문자를 제거하고 사전식으로 정렬한다는 말이 어렵다.
# 즉, 중복된 문자를 제거하되 마지막 한개 남은 문자라면 그 자리에 남겨두고 뒤에 중복문자가 있다면 앞에 있는 중복 문자를 없애버린다.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        strset = set(s)
        stack, counter = [], collections.Counter(s)
        for ch in s:
            counter[ch] -= 1
            if ch in stack:
                continue
            while stack and ch < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)

        return ''.join(stack)