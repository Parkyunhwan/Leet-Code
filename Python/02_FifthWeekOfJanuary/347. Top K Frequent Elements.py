import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = collections.Counter(nums)
        ret = []
        li = counters.most_common(k)
        for l in li:
            ret.append(l[0])
        return ret

# heapq(우선순위큐)를 이용한 방법
# 파이썬은 min heap만 지원하기 때문에 key에 해당하는 값을 음수로 취하면 max heap처럼 사용할 수 있다.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

# 내 코드에서 더 개선된 파이썬 풀이법
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(zip(*collections.Counter(nums).most_common(k)))
