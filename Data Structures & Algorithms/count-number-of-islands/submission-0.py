
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Loop through the list.
        # Detect 1's and start DFS.
        # Add 1s to visited once DFS is run on an island.
        # Next DFS run will be for a separate 1, not included in visited.

        islands = 0
        # Needs persistance --> Iterative DFS

        for row in range(len(grid)):  # Row
            for col in range(len(grid[0])): # Col
                if grid[row][col] == "1":
                    grid = self.dfs(grid, row, col)
                    islands += 1

        return islands
        
    # Converts all 1s into 0s within an island.
    def dfs(self, grid:List[List[str]], start_row:int, start_col:int) -> List[List[str]]:
        # Now dfs starting from input cell, covering all 1s in the island.
        # Get all of them first, then sink them (convert to 0).

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        to_sink = {}    # Don't need order so SET.

        stack = [(start_row, start_col)]

        while stack:
            row, col = stack.pop()
            grid[row][col] = "0"

            for drow, dcol in directions:
                new_row = row + drow
                new_col = col + dcol

                if (0 <= new_row and new_row < len(grid) and 0 <= new_col and new_col < len(grid[0])) and grid[new_row][new_col] == "1":
                    stack.append((new_row, new_col))
        return grid






            




        


