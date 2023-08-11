# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for l in lists:
            while l is not None:
                nums.append(l.val)
                l = l.next
        answer = ListNode()
        temp = answer
        for num in sorted(nums):
            temp.next = ListNode(val=num)
            temp = temp.next
        return answer.next
        
        
