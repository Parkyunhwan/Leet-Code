# My solution
# 책 풀이보다 두배 정도 속도는 빠름 (거리 갱신시에만 넣어서 그런듯..?)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, cost in flights:
            graph[a].append((b, cost))

        dist = [sys.maxsize] * n

        q = [(-1, 0, src)]
        result = []
        while q:
            k_num, time, node = heapq.heappop(q)
            if node == dst and k_num <= K: # 경우의 수는 모두 체크하고 경유지 갯수가 이하인 것만 결과에 추가...(모든 경우 검사하므로 더 오래걸림)
                result.append(time)
            if k_num <= K:
                for nxt, cost in graph[node]:
                    if dist[nxt] > time + cost:
                        dist[nxt] = time + cost
                        heapq.heappush(q, (k_num + 1, time + cost, nxt))
        return min(result) if result else -1


# Book Solution
'''
전체 거리를 보관할 필요가 없기 때문에 dist 딕셔너리를 쓰지 않는다고 한다.
오직 최단 거리만 필요하기 때문에 그 값만 저장한다.
경유지를 넘어서는 경우는 아예 우선순위 큐에 삽입하지 않도록 한다.

K 경우를 좀 더 직관적으로 처리하기 위해 K를 넣고 갯수를 점차 빼나가도록 처리했다.
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, cost in flights:
            graph[a].append((b, cost))

        dist = [sys.maxsize] * n

        q = [(0, src, K)]
        result = []
        while q:
            price, node, k = heapq.heappop(q)
            if node == dst:
                return price  # 우선순위 큐이기 때문에 최단거리가 나오며, 경유지가 K개 이상인 값도 절대 나올수 없다.
            if K >= 0:
                for v, w, in graph[node]:
                    alt = price + w
                    heapq.heappush(q, (alt, v, k - 1))
        return -1

