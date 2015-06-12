# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.curr = TreeNode(float('-inf'))

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.__helper(self.root)

    # @return an integer, the next smallest number
    def next(self):
        return self.curr.val
        
    def __helper(self, node):
        if node == None:
            return False
        
        elif self.curr.val < node.val:
            ret = self.__helper(node.left)
            if not ret:
                self.curr = node
            return True
        else:
            return self.__helper(node.right)
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

n = TreeNode(1)

s = BSTIterator(n)
