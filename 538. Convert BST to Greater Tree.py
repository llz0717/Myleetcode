# this is a super hard problem
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.ct += root.val
            root.val = self.ct
            dfs(root.left)
        self.ct = 0
        dfs(root)
        return root
