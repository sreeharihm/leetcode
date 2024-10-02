
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 =ListNode(0)
        curr = l3
        carry=0
        while l1!=None or l2!=None or carry !=0:
            l1val= l1.val if l1 else 0
            l2val= l2.val if l2 else 0
            sum = l1val+l2val+carry
            carry= sum//10
            sum= sum%10 
            temp =ListNode(sum,None)  
            curr.next = temp
            curr = temp 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l3.next

a = Solution()
l1 = ListNode(2,None)
l1.next = ListNode(4,None)
l1.next.next=ListNode(3,None)

l2 = ListNode(5,None)
l2.next = ListNode(6,None)
l2.next.next=ListNode(4,None)

print(a.addTwoNumbers(l1,l2))
