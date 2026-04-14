from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid = self.bfs(grid, row, col)
                    num += 1
        
        return num
        
    
    def bfs(self, grid, row:int, col:int) -> List[List[str]]:
        queue = deque([(row, col)])
        grid[row][col] = "0"

        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
               

                if x < len(grid)-1 and grid[x+1][y] == "1":
                    grid[x+1][y] = "0"
                    queue.append((x+1, y))
                if x > 0 and grid[x-1][y] == "1":
                    grid[x-1][y] = "0"
                    queue.append((x-1, y))
                if y < len(grid[0])-1 and grid[x][y+1] == "1":
                    grid[x][y+1] = "0"
                    queue.append((x, y+1))
                if y > 0 and grid[x][y-1] == "1":
                    grid[x][y-1] = "0"
                    queue.append((x, y-1))
        return grid





            




        


