

class Solution {
    int target;
    Set<Integer> map = new HashSet<>();
    Map<Integer, Set<Integer>> dp = new HashMap<>();

    public boolean getAnswer(int stone, int k) {
        if (stone == target) return true;
        else if (!map.contains(stone)) return false;
        else if (!dp.containsKey(stone))
            dp.put(stone, new HashSet<>());

        Set<Integer> set = dp.get(stone);
        if (!set.contains(k)) {
            int nextStone = stone+k;
            if (
                (k-1>0 && getAnswer(nextStone-1, k-1))
                || (k>0 && getAnswer(nextStone, k))
                || getAnswer(nextStone+1, k+1)
            )
                return true;
            set.add(k);
        }
        return false;
    }

    public boolean canCross(int[] stones) {
        for (var stone: stones) 
            map.add(stone);
        target = stones[stones.length-1];
        return getAnswer(0, 0);
    }
}