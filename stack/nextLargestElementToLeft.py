from stacks import Stack
arr = [1,3,2,4]
nextLargest =[]
s1 = Stack()
for i in range(0, len(arr)):
    while not s1.isEmpty() and s1.top()<= arr[i]:
        s1.pop()
    if s1.isEmpty():
        nextLargest.append(-1)
    else:
        nextLargest.append(s1.top())
    s1.push(arr[i])
print(nextLargest)            