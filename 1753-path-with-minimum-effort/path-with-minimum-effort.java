class Solution {
    public class Node {
        public int x;
        public int y;
        public int cost;
        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
        @Override
        public String toString() {
            return String.format("(x=%d, y=%d, cost=%d)", x, y, cost);
        }
    }
    public int minimumEffortPath(int[][] heights) {
        int[][] done = new int[heights.length][heights[0].length];        
        int[][] ds = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        done[0][0] = 1;
        PriorityQueue<Node> nodes = new PriorityQueue<>(
            (Node node1, Node node2) -> node1.cost - node2.cost
        );
        if (heights.length > 1)
            nodes.add(new Node(1, 0, 1 + Math.abs(heights[0][0]-heights[1][0])));
        if (heights[0].length > 1)
            nodes.add(new Node(0, 1, 1 + Math.abs(heights[0][0]-heights[0][1])));
        while (done[heights.length-1][heights[0].length-1] == 0) {
            Node node = nodes.poll();
            if (done[node.x][node.y] == 0) {
                done[node.x][node.y] = node.cost;
                for (var d: ds) {
                    int nx = node.x + d[0];
                    int ny = node.y + d[1];
                    if (
                        nx >= 0 && nx < heights.length 
                        && ny >= 0 && ny < heights[0].length
                        && done[nx][ny] == 0
                    ) {
                        nodes.add(
                            new Node(nx, ny, Math.max(
                            node.cost, 1 + Math.abs(
                                heights[node.x][node.y] - heights[nx][ny]
                            )
                        )));
                    }
                }
            }
        }
        return done[heights.length-1][heights[0].length-1]-1;
    }
}