class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        ret = []

        pre = [1]

        ret.append(pre)

        row = []
        for i in range(0,numRows -1):
            row.append(1)
            for j in range(len(pre) -1):
                row.append(pre[j] + pre[j+1])
            row.append(1)
            pre = row
            row = []
            ret.append(pre)
        return ret