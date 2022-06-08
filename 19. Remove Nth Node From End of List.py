class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        counter=0
        pass1=pass2=head
        while head:
            head=head.next
            counter+=1
        if counter-n==0:
            return pass1.next       
        index=1
        while pass2:
            if index== (counter-n):
                pass2.next=pass2.next.next  
                return pass1
            
            pass2=pass2.next
            index+=1
