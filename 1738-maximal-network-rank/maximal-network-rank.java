class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        List<Map<Integer, Boolean>> edges = new ArrayList<Map<Integer, Boolean>>();
        for (int i=0; i<=n; i++)
            edges.add(new HashMap<Integer, Boolean>());
        
        for (var road: roads) {
            edges.get(road[0]).put(road[1],true);
            edges.get(road[1]).put(road[0],true);
        }

        int answer = 0;

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                answer = Math.max(
                    answer,
                    edges.get(i).size() + edges.get(j).size() - (edges.get(i).containsKey(j) ? 1 : 0)
                );
            }
        }

        return answer;
    }
}