# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#O(n) time, O(1) space

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode
        return prevNode


        