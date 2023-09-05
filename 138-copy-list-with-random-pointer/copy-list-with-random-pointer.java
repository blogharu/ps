/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head != null) {
            Map<Node, Node> map = new HashMap<>();
            Node node = head;
            map.put(node, new Node(node.val));
            while (node.next != null) {
                node = node.next;
                map.put(node, new Node(node.val));
            }
            Node answer = map.get(head);
            if (head.random != null)
                answer.random = map.get(head.random);
            node = answer;
            while (head.next != null) {
                head = head.next;                
                node.next = map.get(head);
                node = node.next;
                if (head.random != null)
                    node.random = map.get(head.random);
            }
            head = answer;
        }
        return head;
    }
}