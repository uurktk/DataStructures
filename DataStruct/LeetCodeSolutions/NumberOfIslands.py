class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        # Iterate over each cell in the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":  # Found an unvisited part of an island
                    island_count += 1
                    # Use a stack to simulate DFS
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                            # Mark the cell as visited
                            grid[x][y] = "v"
                            # Add all neighboring cells to the stack
                            stack.append((x - 1, y))  # up
                            stack.append((x + 1, y))  # down
                            stack.append((x, y - 1))  # left
                            stack.append((x, y + 1))  # right
        return island_count    