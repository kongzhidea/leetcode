# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isMiroTree(root.left,root.right)
    def isMiroTree(self, p, q):
        if p == None and q == None:
            return True
        if p!=None and q == None:
            return False
        if q!=None and p == None:
            return False
        if(p.val != q.val):
            return False
        if not self.isMiroTree(p.left,q.right):
            return False
        if not self.isMiroTree(p.right,q.left):
            return False
        return True