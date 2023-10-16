import java.math.BigInteger;

class Solution {
    BigInteger[] factorials = new BigInteger[34];
    public int getComb(int n, int k) {
        return factorials[n].divide(factorials[k]).divide(factorials[n-k]).intValue();
    }
    public List<Integer> getRow(int rowIndex) {
        factorials[0] = BigInteger.ONE;
        for (int i = 1; i <= rowIndex; i++)
            factorials[i] = factorials[i-1].multiply(BigInteger.valueOf(i));
        List<Integer> answer = new ArrayList<>(List.of(1));
        for (int i = 1; i <= rowIndex; i++)
            answer.add(getComb(rowIndex, i));
        return answer;
    }
}