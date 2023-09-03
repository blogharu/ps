/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";
        return String.format(
            "v=%d,l=(%s),r=(%s)", root.val, serialize(root.left), serialize(root.right)
        );  
    }

    public TreeNode deserialize(String data) {
        if (data.length() == 0) return null;
        int valStart = data.indexOf('=')+1;
        int valEnd = data.indexOf(',', valStart);
        int val = Integer.parseInt(data.substring(valStart, valEnd));
        TreeNode answer = new TreeNode(val);

        valStart = data.indexOf('(', valEnd)+1;
        int count = 1;
        for (int i=valStart; i<data.length(); i++) {
            char c = data.charAt(i);
            switch(c) {
                case '(':
                    count ++;
                    break;
                case ')':
                    count --;
                    break;
            }
            if (count == 0) { 
                answer.left = deserialize(data.substring(valStart, i)); 
                valStart = data.indexOf('(', i)+1;
                break;
            }
        }
        count = 1;
        for (int i=valStart; i<data.length(); i++) {
            char c = data.charAt(i);
            switch(c) {
                case '(':
                    count ++;
                    break;
                case ')':
                    count --;
                    break;
            }
            if (count == 0) { answer.right = deserialize(data.substring(valStart, i)); break;}
        }
        return answer;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));