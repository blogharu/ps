class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> answer = new ArrayList<>();

        int length = 0;
        Deque<String> deque = new LinkedList<>();

        for (var word: words) {
            int space = deque.size();
            if (length + space + word.length() <= maxWidth) {
                length += word.length();
                deque.add(word); 
            } else {
                int numSpaces = maxWidth - length;
                int numWords = deque.size();
                if (numWords > 1) {
                    int defaultSpace = numSpaces / (numWords - 1);
                    int extra = numSpaces % (numWords - 1);   
                    for (int i=0; i<numWords-1; i++) {
                        deque.add(deque.pollFirst());
                        deque.add(" ".repeat(defaultSpace + (extra-- > 0 ? 1 : 0)));
                    }
                    deque.add(deque.pollFirst());
                } else {
                    deque.add(" ".repeat(numSpaces));
                }
                answer.add(String.join("", deque));
                deque.clear();
                deque.add(word);
                length = word.length();
            }
        }
        if (length + deque.size() - 1 < maxWidth)
            deque.add(" ".repeat(maxWidth-(length + deque.size() - 1)-1));
        answer.add(String.join(" ", deque));
        return answer;
    }
}