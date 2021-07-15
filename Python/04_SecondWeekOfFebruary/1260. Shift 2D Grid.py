class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        while k:
            for i in range(len(grid)):
                grid[i] = [grid[i][-1]] + grid[i][:-1]

            m = len(grid)
            save = grid[m - 1][0]
            li = []
            for i in range(m - 1):
                li.append(grid[i][0])
            grid[0][0] = save
            for i in range(1, m):
                grid[i][0] = li[i - 1]
            k -= 1
        return grid