class Stack:
    def __init__(self):
        self.stack = []
        self.top_index = -1

    def push(self, element):
        self.stack.append(element)
        self.top_index += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped = self.stack[self.top_index]
        self.stack.pop()
        self.top_index -= 1
        return popped

    def traverse(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        for i in range(self.top_index, -1, -1):
            print(self.stack[i])

    def isEmpty(self):
        if self.top_index == -1:
            return True
        return False
    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[self.top_index]


