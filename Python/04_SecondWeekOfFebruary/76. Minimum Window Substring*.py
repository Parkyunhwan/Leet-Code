# 정답 ㅠㅠㅠ 어렵다.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)  # hash table to store char frequency
        missing = len(t)  # total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):  # index j from 1 # 오직 j의 인덱스 값만 1부터 시작하게 된다.
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            # print(j, char, need[char], missing)
            if missing == 0:  # match all chars
                # while문을 돌면서 t에 들어있지 않는 문자나 중복된 문자를 제거하도록 한다. (핵심)
                while i < j and need[s[i]] < 0:  # remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1  # make sure the first appearing char satisfies need[char]>0
                missing += 1  # we missed this first char, so add missing by 1
                # print(s[i:j])
                if end == 0 or j - i < end - start:  # update window
                    start, end = i, j

                i += 1  # update i to start+1 for next window
        return s[start:end]

# O(n^2)의 시간복잡도의 브루트포스 풀이법
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr, t):
            # t의 모든 문자에 대해 substr을 검사하며 만약 있다면 삭제해둔다. (중복 방지)
            for char in t:
                if char in s_substr:
                    s_substr.remove(char)
                else:
                    return False
            return True

        t_len = len(t)
        set_t = set(t)
        # 먼저 슬라이딩 윈도우 크기를 선택한다.
        for w_len in range(t_len, len(s) + 1):
            # 모든 시작위치에서 슬라이딩 윈도우를 검사한다. (전체 슬라이딩 윈도우를 잡을 수 없는 것은 이미 검사했으므로 필요없음 (len(s) - w_len + 1))
            for start in range(len(s) - w_len + 1):
                substr = s[start:start + w_len]
                # substr에 t의 문자들이 모두 포함되었는 지 검사한다.
                if contains(list(substr), list(t)):
                    return substr
        return ''

# 슬라이딩 윈도우 + 투 포인터로 풀었지만 시간초과 ㅠㅠ
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_sub, t):
            for char in t:
                if char in s_sub:
                    s_sub.remove(char)
                else:
                    return False
            return True

        left = 0
        right = t_len = len(t)
        s_len = len(s)
        result = ''
        while left < s_len - t_len + 1:
            substr = s[left:right]
            if contains(list(substr), list(t)):
                if not result:
                    result = substr
                elif len(result) > len(substr):
                    result = substr
                left += 1
                continue
            if right <= len(s):
                right += 1
            else:
                left += 1
        return result

