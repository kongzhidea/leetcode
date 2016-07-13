class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        return self.validateRow(board) and self.validateCol(board) and  self.validateBox(board)

    def validateBox(self,board):
        r = 9
        for i in xrange(r):
            count = [0] * 10
            sr = 3* (i/3)
            sc = 3* (i%3)
            for j in xrange(3):
                for k in xrange(3):
                    n = board[sr + j][sc + k]
                    if n == '.':
                        continue
                    n = int(n)
                    count[n] += 1
                    if count[n] > 1:
                        return False
        return True

    def validateCol(self,board):
        r = 9
        for i in xrange(r):
            count = [0] * 10
            for j in xrange(r):
                n = board[j][i]
                if n == '.':
                    continue
                n = int(n)
                count[n] += 1
                if count[n] > 1:
                    return False
        return True

    def validateRow(self,board):
        r = 9
        for i in xrange(r):
            count = [0] * 10
            for j in xrange(r):
                n = board[i][j]
                if n == '.':
                    continue
                n = int(n)
                count[n] += 1
                if count[n] > 1:
                    return False
        return True