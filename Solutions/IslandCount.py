class Solution:
    def verify_land_or_water(self, grid, r, c, visited):
        # check boundaries of r and c
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
            return False

        # return false if water
        if grid[r][c] == '0':
            return False

        position = '{r}, {c}'.format(r=r, c=c)
        if position in visited:
            return False
        visited.add(position)

        # DFS
        self.verify_land_or_water(grid, r-1, c, visited)
        self.verify_land_or_water(grid, r+1, c, visited)
        self.verify_land_or_water(grid, r, c-1, visited)
        self.verify_land_or_water(grid, r, c+1, visited)

        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.verify_land_or_water(grid, r, c, visited):
                    count += 1
        return count
