# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head:
            lt, gte = [], []
            temp = head
            while temp:
                lt.append(temp.val) if temp.val < x else gte.append(temp.val)
                temp = temp.next
            temp = head
            for stack in [lt, gte]:
                for v in stack:
                    temp.val = v
                    temp = temp.next
        return head