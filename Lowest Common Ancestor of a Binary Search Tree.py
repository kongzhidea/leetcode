# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if(root==None or  p==None or q==None):
            return None;

        if(max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q);
        elif(min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q);
        else:
            return root;