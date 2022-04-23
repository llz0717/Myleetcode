class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stacks,ans=[root],[]
        while stacks:
            cur=stacks.pop()
            
            if cur:
                ans.append(cur.val)
                stacks.append(cur.right)
                stacks.append(cur.left)        
        return ans
