class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for a, b, cost in times:
            graph[a].append((b, cost))

        q = [(0, k)]
        dist = collections.defaultdict(int)

        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
        print(dist)
        if len(dist) == n:
            return max(dist.values())
        return -1

