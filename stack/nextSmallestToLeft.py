from stacks import Stack
arr = [4,5,2,10,8]
# output:[-1,4,-1,2,2]
nextSmallLeft = []
s1 = Stack()
for i in range(0,len(arr)):
    while not s1.isEmpty() and s1.top()>= arr[i]:
        s1.pop()
    if s1.isEmpty():
        nextSmallLeft.append(-1)
    else:
        nextSmallLeft.append(s1.top())
    s1.push(arr[i])

print(nextSmallLeft)


 
