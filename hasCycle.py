from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow != None and fast != None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                continue
            else:
                fast = fast.next
            if slow == fast:
                return True
        return False
    
a=Solution()
list1 = ListNode(1,None)
list1.next = ListNode(2,None)
list1.next.next=ListNode(4,None)
list1.next.next.next=ListNode(5,list1.next)
print(a.hasCycle(list1))