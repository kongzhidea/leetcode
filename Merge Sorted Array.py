class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        ret = []
        pa = 0;pb = 0
        while pa < m or pb <n:
            if pa < m and pb < n:
                if A[pa] < B[pb]:
                    ret.append(A[pa])
                    pa +=1
                else:
                    ret.append(B[pb])
                    pb +=1
                continue
            if pb < n:
                ret.append(B[pb])
                pb +=1
                continue
            if pa < m:
                ret.append(A[pa])
                pa +=1
                continue

        while len(A) >0:
            A.pop()
        for c in ret:
            A.append(c)