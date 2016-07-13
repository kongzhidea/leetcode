class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        ret = []
        pts = path.split("/")
        for pt in pts:
            if pt == "":
                continue
            if pt == ".":
                continue
            if pt == "..":
                if len(ret) > 0:
                    ret.pop()
                continue
            ret.append(pt)
        return "/" + "/".join(ret)