class Solution {
    class Element {
        int count;
        int val;
        Element(int count, int val) {
            this.count = count;
            this.val = val;
        }
        public String toString() {
            return String.format("(%d, %d)", count, val);
        }
    }
    public int minDeletions(String s) {
        int answer = 0;
        int []counts = new int[26];

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            counts[c-'a']++;
        }

        PriorityQueue<Element> pq = new PriorityQueue<>(
            (e1, e2) -> e2.count - e1.count
        );

        for (int i=0; i<counts.length; i++) {
            if (counts[i] != 0) {
                pq.add(new Element(counts[i], i));
            }
        }

        while(pq.size() > 0) {
            Element ele = pq.poll();
            while(pq.size() > 0) {
                if (pq.peek().count != ele.count) break;
                Element temp = pq.poll();
                temp.count--;
                answer++;
                if (temp.count > 0) pq.add(temp);
            }
        }

        return answer;
    }
}