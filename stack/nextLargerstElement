from stacks import Stack
 # Main code to find the next largest element
arr = [1, 3, 2, 4]
nextLargestElement = []
s1 = Stack()

# Iterate through the array from the end to the beginning
for i in range(len(arr) - 1, -1, -1):
    while not s1.isEmpty() and s1.top() <= arr[i]:
        s1.pop()

    if s1.isEmpty():
        nextLargestElement.append(-1)
    else:
        nextLargestElement.append(s1.top())

    s1.push(arr[i])

# Since we processed elements from end to start, reverse the result to correct the order
nextLargestElement.reverse()

print(nextLargestElement)
