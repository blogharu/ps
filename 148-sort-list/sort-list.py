# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappop

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            arr = []
            temp = head
            while temp:
                arr.append(temp.val)
                temp = temp.next
            heapify(arr)
            temp = head
            while temp:
                temp.val = heappop(arr)
                temp = temp.next
        return head
