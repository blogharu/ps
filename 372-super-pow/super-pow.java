class Solution {
    int MOD = 1337;
    public int superPow(int a, int[] b) {
        long []answers = new long[MOD*3];
        int i = 0, power = 0, loop = 0;
        {
            long temp = 1;
            Set<Long> set = new HashSet<>();
            for(; !set.contains(temp); i++) {
                answers[i] = temp;
                set.add(temp);
                temp = (temp * a) % MOD;
            }
            long target = temp;
            do {
                temp = (temp * a) % MOD;
                loop++;
            } while (temp != target);
        }

        int j = 0;
        for (; j < b.length-4; j++) {
            power = (power * 10 + b[j]) % loop;
        }
        for (; j < b.length; j++) {
            power = power * 10 + b[j];
        }
        if (i != loop) {
            power = ((power-i+loop)%loop) + i-loop;
        }
        return (int) answers[power%i];
    }
}