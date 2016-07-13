# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.balance = True
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        self.dfs(root)
        return self.balance

    def dfs(self,root):
        if not self.balance:
            return -1
        if root == None:
            return 0
        lheight = self.dfs(root.left) 
        rheight = self.dfs(root.right)

        deta = abs(lheight - rheight)
        if deta > 1:
            self.balance = False
            return -1
        return max(lheight,rheight) + 1
        