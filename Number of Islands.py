class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        ln = len(grid)
        if ln == 0:
            return 0
        lm = len(grid[0])
        count = 0
        use = [ [ 0 for col in xrange(lm)] for row in xrange(ln) ]
        for i in xrange(ln):
            for j in xrange(lm):
                if grid[i][j] == '1' and use[i][j] == 0:
                    self.trace(i,j,grid,use)
                    count += 1
        return count
    def trace(self,i,j,grid,use):
        ln = len(grid)
        lm = len(grid[0])

        queue = []
        queue.append([i,j])
        use[i][j] = 1
        while len(queue) > 0:
            r,c = queue[0]
            queue = queue[1:]
            if r + 1< ln and use[r+1][c] == 0 and grid[r+1][c] == "1":
                use[r+1][c] = 1
                queue.append([r+1,c])
            if r - 1 >= 0 and use[r-1][c] == 0 and grid[r-1][c] == "1":
                use[r-1][c] = 1
                queue.append([r-1,c])
            if c + 1 < lm and use[r][c+1] == 0 and grid[r][c+1] == "1":
                use[r][c+1] = 1
                queue.append([r,c+1])
            if c -1 >= 0 and use[r][c - 1] == 0 and grid[r][c-1] == "1":
                use[r][c - 1] = 1
                queue.append([r,c-1])