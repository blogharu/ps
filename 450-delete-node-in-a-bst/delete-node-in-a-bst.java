/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        var isLeft = true;
        var prevNode = root;
        var node = root;
        while (node != null && node.val != key) {
            prevNode = node; 
            if (node.val > key) {
                node = node.left;
                isLeft = true;
            }
            else {
                node = node.right;
                isLeft = false;
            }
        }        
        if (node != null) {
            while (node.left != null || node.right != null) {
                if (node.left != null) {
                    TreeNode nextNode = node.left;                    
                    if (nextNode.right == null) {
                        node.val = nextNode.val;
                        node.left = nextNode.left;
                        return root;
                    }
                    else {
                        if (isLeft) prevNode.left = nextNode;
                        else prevNode.right = nextNode;
                        node.left = nextNode.right;
                        nextNode.right = node;
                        prevNode = nextNode;
                        isLeft = false;
                        if (root == node) root = prevNode;
                    }
                }
                else {
                    TreeNode nextNode = node.right;                    
                    if (nextNode.left == null) {
                        node.val = nextNode.val;
                        node.right = nextNode.right;
                        return root;
                    }
                    else {
                        if (isLeft) prevNode.left = nextNode;
                        else prevNode.right = nextNode;
                        node.right = nextNode.left;
                        nextNode.left = node;
                        prevNode = nextNode;
                        isLeft = true;
                        if (root == node) root = prevNode;
                    }
                }
            }
            if (prevNode == node) return null;
            else if (isLeft) prevNode.left = null;
            else prevNode.right = null;
        }
        return root;
    }
}