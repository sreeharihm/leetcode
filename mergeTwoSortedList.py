from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode()
        dd = dummy
        while head1 and head2:
            if head1.val<= head2.val:
                new= ListNode(head1.val,None)
                dd.next = new
                dd = new
                head1 = head1.next
            else:
                new =ListNode(head2.val,None)
                dd.next = new
                dd = new
                head2=head2.next
        
        while head1:
            new =ListNode(head1.val,None)
            dd.next  =new
            dd = new
            head1 =head1.next
        while head2:
            new =ListNode(head2.val,None)
            dd.next = new
            dd = new
            head2 =head2.next
        return dummy.next
    
a = Solution()
list1 = ListNode(1,None)
list1.next = ListNode(2,None)
list1.next.next=ListNode(4,None)
list2 = ListNode(1,None)
list2.next = ListNode(3,None)
list2.next.next = ListNode(4,None)
print(a.mergeTwoLists(list1,list2))  