class MyStack {
    boolean isA;
    Queue<Integer> a, b, q;

    public MyStack() {
        isA = true;
        a = new LinkedList<>();
        b = new LinkedList<>();
    }
    
    public void push(int x) {
        q = isA ? a : b;
        q.add(x);
        isA = !isA;
    }
    
    public int pop() {
        q = !isA ? a : b;
        isA = !isA;
        for (int i=0; i<q.size()-1; i++)
            q.add(q.poll());
        return q.poll();
    }
    
    public int top() {
        q = !isA ? a : b;
        for (int i=0; i<q.size()-1; i++)
            q.add(q.poll());
        int top = q.peek();
        q.add(q.poll());
        return top;
    }
    
    public boolean empty() {
        return a.peek() == null && b.peek() == null;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */