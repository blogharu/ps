import java.util.LinkedList;

class Node {
    int x;
    int y;
    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    int[][] mat;
    LinkedList<Node> nodes = new LinkedList<Node>();

    boolean isUpdate(int i, int j, int val) {
        if (i > 0 && mat[i-1][j] != val) return false;
        if (i+1 < mat.length && mat[i+1][j] != val) return false;
        if (j > 0 && mat[i][j-1] != val) return false;
        if (j+1 < mat[0].length && mat[i][j+1] != val) return false;
        return true;
    }

    void update() {
        for (Node node: nodes) { 
            mat[node.x][node.y]++; 
        }
        LinkedList<Node> nextNodes = new LinkedList<Node>();
        for (Node node: nodes) { 
            if (isUpdate(node.x, node.y, mat[node.x][node.y])) {
                nextNodes.add(new Node(node.x, node.y));
            }
        }
        nodes = nextNodes;
    }
    public int[][] updateMatrix(int[][] mat) {
        this.mat = mat;
        for (int i=0; i < mat.length; ++i) {
            int[] row = mat[i];
            for (int j=0; j < row.length; ++j) {
                int val = row[j];
                if(val == 1 && isUpdate(i, j, val)) {
                    nodes.add(new Node(i,j));
                }
            }
        }
        while (nodes.size() > 0) {
            update();
        }
        return mat;
    }
}