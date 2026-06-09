class MinStack:

    def __init__(self):
        self.main = []
        self.min_tracker = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if self.min_tracker:
            self.min_tracker.append(min(val, self.min_tracker[-1]))
        else:
            self.min_tracker.append(val)

    def pop(self) -> None:
        self.main.pop()
        self.min_tracker.pop()
    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1]
        
