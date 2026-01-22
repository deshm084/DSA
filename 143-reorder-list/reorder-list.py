# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head 
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev =  None
        curr = slow.next
        slow.next =None 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next 
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


        