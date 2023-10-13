class Solution {
    public boolean isMatch(String s, String p) {
        int si = 0, pi = 0, ppi = -1, ssi = -1, pLength = p.length(), sLength=s.length();
        while (si < sLength) {
            if (pi < pLength && (p.charAt(pi) == '?' || p.charAt(pi) == s.charAt(si))) {
                pi++;
                si++;
            }
            else if (pi < pLength && p.charAt(pi) == '*') {
                ppi = ++pi;
                ssi = si;
            }
            else if (ppi == -1) { return false; }
            else {
                pi = ppi;
                si = ssi++;
            }
        }
        while (pi < pLength && p.charAt(pi) == '*') ++pi;
        return pi == pLength;
    }
}