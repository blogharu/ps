/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (left != right) {
            int []vals = new int[right-left+1];
            ListNode temp = head;
            for (int i=0; i<left-1; i++)
                temp = temp.next;
            {
                ListNode n = temp;
                for (int i=0; i<vals.length; i++) {
                    vals[i] = n.val;
                    n = n.next;
                }
            }
            for (int i=vals.length-1; i>=0; i--) {
                temp.val = vals[i];
                temp = temp.next;
            }
        }
        return head;
    }
}