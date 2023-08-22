class Solution {
    public String convertToTitle(int columnNumber) {
        Deque<String> deque = new LinkedList<>();
        int length = 1;
        int check = 26;
        columnNumber--;
        for (; length < 7; length++) {
            if (columnNumber >= check) {
                columnNumber -= check;
                check *= 26;
                continue;
            }
            break;
        }
        while (columnNumber != 0) {
            deque.addFirst(""+(char)('A'+columnNumber%26));
            columnNumber /= 26;
        }
        while (length != deque.size()) {
            deque.addFirst(""+'A');
        }
        return String.join("", deque);
    }
}