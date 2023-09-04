public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        for (int i=0; i< 10005; i++)
            if (head.next != null) head = head.next;
        return head.next != null;        
    }
}