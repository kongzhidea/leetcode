class Stack {
private:
    queue<int> que[2];
    int cur = 0;
    
public:
    // Push element x onto stack.
    void push(int x) {
        que[cur].push(x);
    }

    // Removes the element on top of the stack.
    void pop(void) {
        while (que[cur].size() > 1) {
            que[1 - cur].push(que[cur].front());
            que[cur].pop();
        }
        que[cur].pop();
        cur = 1 - cur;
    }

    // Get the top element.
    int top(void) {
        while (que[cur].size() > 1) {
            que[1 - cur].push(que[cur].front());
            que[cur].pop();
        }
        int top = que[cur].front();
        que[1 - cur].push(que[cur].front());
        que[cur].pop();
        cur = 1 - cur;
        return top;
    }

    // Return whether the stack is empty.
    bool empty(void) {
        return que[cur].empty();
    }
};