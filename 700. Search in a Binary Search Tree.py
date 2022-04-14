# Binary Search Tree is a binary tree where the key in each node
# is greater than any key stored in the left sub-tree,
# and less than any key stored in the right sub-tree.

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val!=val:
            root=root.left if root.val>val else root.right
        return root
        
