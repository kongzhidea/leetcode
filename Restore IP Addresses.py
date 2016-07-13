class Solution:
    # @param s, a string
    # @return a string[]
    def restoreIpAddresses(self, s):
        if s == "" or s == None:
            return []
        ret = []
        ln = len(s)
        for i in xrange(1,ln-2):
            ip1 = s[0:i]
            if not self.validateIp(ip1):
                continue
            for j in xrange(i+1,ln-1):
                ip2 = s[i:j]
                if not self.validateIp(ip2):
                    continue
                for k in xrange(j+1,ln):
                    ip3 = s[j:k]
                    if not self.validateIp(ip3):
                        continue
                    ip4 = s[k:ln]
                    if not self.validateIp(ip4):
                        continue
                    ret.append(ip1 + "." + ip2 + "." + ip3 + "." + ip4)
        return ret
    def validateIp(self,subip):
        if subip == "" or len(subip) >3:
            return False
        if int(subip) !=0 and subip.startswith("0"):
            return False
        if int(subip) == 0 and len(subip) >1:
            return False
        if int(subip) >=0 and int(subip) <=255 :
            return True
        return False