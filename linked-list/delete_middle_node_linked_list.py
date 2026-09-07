# 2095, Delete Middle Node of Linked List, Linked Lists, Medium
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        
        return dummy.next