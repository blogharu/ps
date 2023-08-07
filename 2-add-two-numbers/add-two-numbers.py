# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        for node in [l1, l2]:
            power = 1
            while node is not None:
                result += node.val * power
                power *= 10
                node = node.next
        answer = ListNode()
        temp = answer
        while result:
            temp.val = result % 10
            result //= 10
            if result:
                temp.next = ListNode()
                temp = temp.next
        return answer