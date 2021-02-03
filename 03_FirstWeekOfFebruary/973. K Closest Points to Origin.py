class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for i in range(len(points)):
            val = pow(points[i][0], 2) + pow(points[i][1], 2)
            points[i].append(val)
        points = sorted(points, key=lambda x: x[2])

        result = []

        for _ in range(K):
            result.append(points.pop(0)[:2])
        return result

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result

