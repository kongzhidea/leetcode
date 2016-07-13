class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        pre = [1]
        row = []
        for i in range(0,rowIndex):
            row.append(1)
            for j in range(len(pre) -1):
                row.append(pre[j] + pre[j+1])
            row.append(1)
            pre = row
            row = []
        return pre