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
    # @return a list of integers
    def postorderTraversal(self, root):
        self.dfs(root)
        return self.ret
    def dfs(self,root):
        if root == None:
            return

        if root.left != None:
            self.dfs(root.left)
        if root.right != None:
            self.dfs(root.right)
        self.ret.append(root.val)