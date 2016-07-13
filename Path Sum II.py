# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ret = []
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root == None:
            return []
        self.dfs(root,sum,[], 0)
        return self.ret
    def dfs(self,root,sum,tmp,total):
        if root.right == None and root.left == None:
            if total + root.val == sum:
                _tmp = tmp[:]
                _tmp.append(root.val)
                self.ret.append(_tmp)
            return
        if root.left != None:
            _tmp = tmp[:]
            _tmp.append(root.val)
            self.dfs(root.left,sum,_tmp,total + root.val)
        if root.right != None:
            _tmp = tmp[:]
            _tmp.append(root.val)
            self.dfs(root.right,sum,_tmp,total + root.val)
        