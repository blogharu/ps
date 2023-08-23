class Count {
    int count;
    String c;
    Count(int count, String c) { this.count=count; this.c=c; }
    public String toString() {
        return c + ", " + count;
    }
}

class Solution {
    PriorityQueue<Count> heap = new PriorityQueue<>((a, b)->b.count-a.count);
    Deque<String> answer = new LinkedList<>();
    int counts[] = new int[26];
    public String reorganizeString(String s) {
        for (int i=0; i<s.length(); i++) {
            int index = s.charAt(i)-'a';
            counts[index]++;
            heap.add(new Count(counts[index], ""+s.charAt(i)));
        }
        int count = 0;
        Count prev = heap.poll();
        answer.add(prev.c);
        while (heap.size() > 0) {
            Count cur = heap.poll();
            if (cur.c.equals(prev.c)) {
                count++;
            } else {
                answer.add(cur.c);
                if (count == 0) {
                    prev = cur;
                } else {
                    answer.add(prev.c);
                    count--;
                }
            }
        }
        return answer.size() == s.length() ? String.join("", answer) : "";
    }
}