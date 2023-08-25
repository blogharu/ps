class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> map = Map.ofEntries(
            Map.entry("I", 1),
            Map.entry("V", 5),
            Map.entry("X", 10),
            Map.entry("L", 50),
            Map.entry("C", 100),
            Map.entry("D", 500),
            Map.entry("M", 1000)
        );
        
        String keys[] = new String[] {"M", "D", "C", "L", "X", "V", "I"};
        int answer = 0;

        for (var key: keys) {
            var splited = s.split(key, -1);
            for (int i = 0; i < splited.length-1; i++)
                answer += map.get(key)-(map.containsKey(splited[i])?map.get(splited[i]):0);
            s = splited[splited.length-1];
            if (s.length() == 0) break;
        }

        return answer; 
    }
}