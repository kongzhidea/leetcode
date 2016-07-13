class Solution:
    def convert_n_bytes(self,n, b):
        bits = b*8
        return (n + 2**(bits-1)) % 2**bits - 2**(bits-1)

    def convert_4_bytes(self,n):
        return self.convert_n_bytes(n, 4)

    def getHashCode(self,s):
        h = 0
        n = len(s)
        for i, c in enumerate(s):
            h = h + c*31**(n-1-i)
        return self.convert_4_bytes(h)
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num,target):
        dt = {}
        ret = []
        use = [0] * len(num)
        num.sort()
        ln = len(num)
        for i in xrange(ln-2):
             use[i] = 1
             for j in xrange(i+1,ln):
                 use[j] = 1
                 st = j+1
                 ed = ln - 1
                 _tot =  (num[i] + num[j]) - target
                 while st < ed:
                     if num[st] + num[ed] == -_tot:
                         tmp = [num[i],num[j],num[st],num[ed]]
                         tmp.sort()
                         code = self.getHashCode(tmp)
                         flag = True
                         if dt.get(code) != None:
                             flag = False
                         if flag == True:
                             dt[code] =  1
                             ret.append(tmp)
                         st +=1
                         ed -=1
                         continue
                     if num[st] + num[ed] < -_tot:
                         st +=1
                     else:
                         ed-=1
                 use[j] = 0
        return ret