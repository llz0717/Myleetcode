class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,ans=[],[]
        cur=root       
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            node=stack.pop()
            ans.append(node.val)
            cur=node.right
        return ans
