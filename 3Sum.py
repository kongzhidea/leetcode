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
        # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        dt = {}
        ret = []
        use = [0] * len(num)
        num.sort()
        ln = len(num)
        for i in xrange(ln):
            use[i] = 1
            st = i+1
            ed = ln - 1
            while st < ed:
                if num[st] + num[ed] == -num[i]:
                    tmp = [num[i],num[st],num[ed]]
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
                if num[st] + num[ed] < -num[i]:
                    st +=1
                else:
                    ed-=1
        return ret