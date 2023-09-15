class Solution {
    class Edge {
        int x, y, cost;
        Edge(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }
    public int minCostConnectPoints(int[][] points) {
        int answer = 0;
        if (points.length > 1) {
            PriorityQueue<Edge> pq = new PriorityQueue<>(
                (Edge e1, Edge e2) -> e1.cost - e2.cost
            );
            for (int i=0; i<points.length; i++) {
                for (int j=i+1; j<points.length; j++) {
                    pq.add(
                        new Edge(i, j, 
                            Math.abs(
                                points[i][0]-points[j][0]
                            ) + 
                            Math.abs(
                                points[i][1]-points[j][1]
                            )
                        )
                    );
                }
            }
            int[] done = new int[points.length];
            Arrays.fill(done, -1);
            List<Integer> updates = new ArrayList<Integer>();
            for(int i=0; i<points.length-1;) {
                Edge edge = pq.poll();
                int x = edge.x;
                int y = edge.y;
                if (done[x] != -1) {
                    while (done[x] != x) {
                        updates.add(x);
                        x = done[x];
                    }
                    while (updates.size() > 0) {
                        done[updates.remove(0)] = x;
                    }
                }
                if (done[y] != -1) {
                    while (done[y] != y) {
                        updates.add(y);
                        y = done[y];
                    }
                    while (updates.size() > 0) {
                        done[updates.remove(0)] = y;
                    }
                }
                if (
                    done[x] >= 0 
                    && done[x] == done[y]
                ) continue;                
                int groupId = Math.min(x, y);
                done[x] = groupId;
                done[y] = groupId;
                answer += edge.cost;
                i++;
            }            
        }
       return answer;
    }
}