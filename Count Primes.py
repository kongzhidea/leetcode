class Solution(object):
    def countPrimes(self, n):
        if n <= 1 :
            return 0
        if n == 2:
            return 0
        # exclude 2
        pri = [0] * (n+1)
        for i in xrange(3,n+1):
            if i & 1 == 1:
                pri[i] = 1
        sq = int(n ** 0.5)
        for i in xrange(3,sq+1,2):
            for j in xrange(i*2,n+1,i):
                if  j > n:
                    break
                pri[j] = 0
        count = 0

        for i in xrange(3,n):
            count +=( 1 if pri[i] == 1  else 0)
        return count + 1