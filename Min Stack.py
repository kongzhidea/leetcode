class MinStack:
    def __init__(self):
        self.data = []
        self.min = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.min) == 0 or x <= self.getMin():
            self.min.append(x)
        self.data.append(x)

    # @return nothing
    def pop(self):
        if self.top()  == self.getMin():
            self.min.pop()
        self.data.pop()

    # @return an integer
    def top(self):
        return self.data[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]