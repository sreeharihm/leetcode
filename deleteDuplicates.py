from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =head
        while (temp and temp.next):
            if temp.val ==temp.next.val:
                temp.next = temp.next.next
                continue
            temp = temp.next
        return head




a = Solution()
list1 = ListNode(1,None)
list1.next = ListNode(1,None)
list1.next.next=ListNode(2,None)
list2 = ListNode(3,None)
list2.next = ListNode(3,None)
list2.next.next = ListNode(4,None)

print(a.deleteDuplicates(list1))