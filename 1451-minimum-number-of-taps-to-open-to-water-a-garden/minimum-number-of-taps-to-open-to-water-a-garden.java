class Solution {
    class Range {
        int start;
        int end;
        Range(int start, int end) {
            this.start = start;
            this.end = end;
        }
        public int getLength() { return this.end - this.start; }
        public String toString() {
            return String.format("Range(start: %d, end: %d, length: %d)", this.start, this.end, this.getLength());
        }
    }

    public int minTaps(int n, int[] _ranges) {
        Range[] ranges = new Range[_ranges.length];
        for (int i=0; i<_ranges.length; i++) {
            ranges[i] = new Range(
                i - _ranges[i] >= 0 ? i-_ranges[i] : 0, 
                i + _ranges[i] <= n ? i + _ranges[i] : n
            );
        }
        Arrays.sort(ranges, 
            (Range a, Range b) -> {
                if (a.end < b.end) return 1;
                else if (b.end < a.end) return -1;
                else if (a.getLength() < b.getLength()) return 1;
                else if (b.getLength() < a.getLength()) return -1;
                return 1;
            }
        );

        int start = n, answer = 0;

        for (var range: ranges) {
            System.out.println(range);
            if (range.getLength() == 0) continue;
            else if (n > range.end) {
                n = start;
                answer++;
                System.out.println(start);
            }
            if (n <= range.end) start = Math.min(start, range.start);
            else return -1;
            if (n == 0) return answer;
        }
        return start==0 ? answer+1 : -1;
    }
}