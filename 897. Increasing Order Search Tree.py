class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        def inOrder(root, res):
            if not root:
                return
            inOrder(root.left, res)
            res.append(root.val)
            inOrder(root.right, res)
            return res
        array = inOrder(root, [])
        root = cur = TreeNode(array[0])
        for i in range(1, len(array)):
            cur.right = TreeNode(array[i])
            cur = cur.right
        return root
