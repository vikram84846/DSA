from stacks import Stack
arr = [4,5,2,10,8]
nextSmallerRight =[]
s1 = Stack()
for i in range(len(arr)-1, -1, -1):
    while not s1.isEmpty() and s1.top()>= arr[i]:
        s1.pop()
    if s1.isEmpty():
        nextSmallerRight.append(-1)
    else:
        nextSmallerRight.append(s1.top())
    s1.push(arr[i])
 
nextSmallerRight.reverse()
print(nextSmallerRight)