# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        queue = []
        ret = []
        queue.append(root)
        while len(queue) > 0:
            line = []
            for i in queue:
                line.append(i.val)
            ret.append(line)
            child = []
            for i in queue:
                if i.left != None:
                    child.append(i.left)
                if i.right != None:
                    child.append(i.right)
            queue = child[:]
        return ret