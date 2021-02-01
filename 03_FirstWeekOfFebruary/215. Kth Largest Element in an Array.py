class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, -num)

        mx = -sys.maxsize
        count = 0
        while q:
            val = heapq.heappop(q)
            count += 1
            if count == k:
                return -val