# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next is not None:
            def swap(node):
                next_node = node.next
                next_next_node = next_node.next
                next_node.next, node.next = node, next_next_node
                return next_node, next_next_node
            prev_node = head
            head, node = swap(head)
            while node is not None and node.next is not None:
                prev_node.next, next_node = swap(node)
                prev_node, node = node, next_node
        return head
        