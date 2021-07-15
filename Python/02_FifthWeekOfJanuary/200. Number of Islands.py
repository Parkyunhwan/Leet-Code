class Solution:
    def bfs(self, i, j, check, grid):
        q = collections.deque()
        q.append((i, j))
        check[i][j] = 1
        while q:
            x, y = q.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                if not check[nx][ny] and grid[nx][ny] == "1":
                    check[nx][ny] = 1
                    q.append((nx, ny))

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        check = [[0] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if check[i][j] == 0 and grid[i][j] == "1":
                    self.bfs(i, j, check, grid)
                    count += 1
        return count