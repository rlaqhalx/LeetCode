# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None
            return head
        fast = head
        slow = head
        prev = head

        for i in range(n):
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if slow == head:
            head = head.next
        
        if prev:
            prev.next= prev.next.next
        
        
            
        return(head)