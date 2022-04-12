class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # creat dummpy listnote
        dummpy = ListNode()
        curp=dummpy
        carry=0
        
        # loop start when there l1 and l2 is not none, and carry is not 0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0  # if not none, give value, else give 0
            val2=l2.val if l2 else 0
            
            sum=val1+val2+carry
            carry=sum//10
            sum=sum%10
            
            # update pointer
            curp.next=ListNode(sum)
            
            
            curp=curp.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        return dummpy.next
