class Solution:
    # 슬라이딩 윈도우와 투포인터에서 유용한 Counter??
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        max_len = 0
        count = collections.Counter()
        for right in range(1, len(s) + 1):
            count[s[right - 1]] += 1
            most = count.most_common(1)[0][1]
            # Counter({'A': 3, 'b' : 2})
            # count.most_common() -> [('A', 3), ('B', 2)]
            # count.most_common(1) -> [('A', 3)]
            # count.most_common(1)[0] -> ('A', 3)
            # count.most_common(1)[0][1] -> 3
            remain = right - left - most
            if remain > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(right - left, max_len) # 이부분을 생략 가능한 이유는
            # 이전 문제와 다르게 최소가 아닌 최대 길이를 구하는 문제이다.
            # 따라서, 한번 증가된 길이를 줄여가며 검사할 필요가 없다. (left와 right가 같이 증가하는 이유)
        # return right - left
        return max_len