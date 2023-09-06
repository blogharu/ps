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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode []answer = new ListNode[k];
        if (head != null) {
            int length = 1;
            {
                ListNode temp = head;
                while (temp.next != null) {
                    temp = temp.next;
                    length++;
                }
            }
            k = Math.min(length, k);
            int mod = length % k;
            length = length / k;
            for (int i=0; i<k; i++) {
                answer[i] = head;
                for (int j=0; j<length+(mod>0?1:0)-1; j++) {
                    head = head.next;
                }
                ListNode temp = head.next;
                head.next = null;
                head = temp;
                mod--;
            }
            System.out.println(length);
        }
        return answer;
    }
}