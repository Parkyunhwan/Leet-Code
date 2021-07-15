class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 슬라이딩 윈도우와 투포인터
        used = dict()
        max_length = start = 0
        for index, char in enumerate(s):
            '''
            이미 있는 문자라면 그 문자 부터 시작위치를 잡아야 하며 시작위치가 이미 그 문자를 넘어갔다면 
            중복되지 않으므로 새롭게 길이를 갱신한다.
            '''
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length
# 시간 초과..
# 모든 시작지점을 검사하기 위해 len(s) - 1를 사용했으므로 1보다 작거나 같은 수에 대한 예외 처리가 필요하다.
# 중복된 지점이 발생한 곳부터 다시 검사해야한다. i -= 1
# 매 반복에 끝마다 현재 리스트를 삭제하기 전에 길이를 최대길이와 비교해서 갱신해야한다.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li = []
        max_length = 0
        j = 0
        if len(s) <= 1:
            return len(s)
        while j < len(s) - 1:
            i = j
            while i < len(s):
                if s[i] not in li:
                    li.append(s[i])
                else:
                    max_length = max(max_length, len(li))
                    li.clear()
                    i -= 1
                i += 1
            max_length = max(max_length, len(li))
            li.clear()
            j += 1
        return max_length