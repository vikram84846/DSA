class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertionAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def insertionAtBeginning(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    def insertionAtPosition(self,data, position):
            if self.head == None:
                self.head = Node(data)
            else:
                tracker = self.head
                for i in range(1, position -1):
                    tracker = tracker.next
                new_node = Node(data)
                new_node.next = tracker.next
                tracker.next = new_node
    def printList(self):
        if self.head == None:
            return ("List is empty")
        else:
            tracker = self.head
            while tracker:
                print("->", tracker.data, end="")
                print()
                tracker = tracker.next
    def deletionAtbeg(self):
      if self.head is None:
        print("empty list ")
      else:
        self.head = self.head.next


    def deletionAtend(self):
      current = self.head
      if self.head is None:
       print("empty list")
      else:
        while current.next.next is not None:
         current = current.next
         current.next = None


    def deletionAtPosition(self,position):
        current = self.head
        if self.head is None:
          print("empty list")
        else:
          for i in range(1,position-1):
            current = current.next
          current.next = current.next.next
    def search(self,target):

      current = self.head
      if self.head is None:
        print("empty list")
      else:
        flag ,position= 0,1
        while current is not None:
          if current.data == target:
           print(f"element {target} is found at position {position}")
           flag = 1
           break
           current = current.next
           position +=1
        if flag == 0:
             print(f"element {target} is not found")
