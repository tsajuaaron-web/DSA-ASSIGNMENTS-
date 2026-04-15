import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 2  # Starting with small capacity as required
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, x):
        if self.size == self.capacity:
            print(f"--- Resizing: Capacity doubled from {self.capacity} to {self.capacity * 2} ---")
            self._resize(2 * self.capacity)
        
        self.array[self.size] = x
        self.size += 1

    def _resize(self, new_cap):
        new_arr = self._make_array(new_cap)
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_cap

    def pop(self):
        if self.size == 0:
            return "Error: Array is empty"
        val = self.array[self.size - 1]
        self.size -= 1
        return val

    def print_array(self):
        elements = [self.array[i] for i in range(self.size)]
        print(f"Array: {elements} | Size: {self.size} | Capacity: {self.capacity}")

# --- Linked List Implementations ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        if not self.head: return
        if self.head.data == x:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != x:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def traverse(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print("SLL:", " -> ".join(map(str, elements)) if elements else "Empty")

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, target, x):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr:
            new_node = Node(x)
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            else:
                self.tail = new_node
            curr.next = new_node

    def delete_at_position(self, pos):
        if not self.head: return
        curr = self.head
        for _ in range(pos):
            if curr.next: curr = curr.next
            else: return
        
        if curr.prev: curr.prev.next = curr.next
        else: self.head = curr.next
            
        if curr.next: curr.next.prev = curr.prev
        else: self.tail = curr.prev

# --- Stack & Queue ---

class Stack:
    def __init__(self):
        self.ll = SinglyLinkedList()

    def push(self, x):
        self.ll.insert_at_beginning(x)

    def pop(self):
        if not self.ll.head: return None
        val = self.ll.head.data
        self.ll.head = self.ll.head.next
        return val

    def peek(self):
        return self.ll.head.data if self.ll.head else None

    def is_empty(self):
        return self.ll.head is None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head: return None
        val = self.head.data
        self.head = self.head.next
        if not self.head: self.tail = None
        return val

# --- Task 4: Application ---

def is_balanced(expr):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping:
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
    return stack.is_empty()

# --- Main Runner (Test Cases) ---
if __name__ == "__main__":
    print("--- Task 1: Dynamic Array ---")
    da = DynamicArray()
    for i in range(1, 11): da.append(i) # Triggering resizes
    da.print_array()
    for _ in range(3): da.pop()
    da.print_array()

    print("\n--- Task 4: Parentheses Checker ---")
    test_cases = ["([])", "([)]", "(((", ""]
    for tc in test_cases:
        print(f"'{tc}': {is_balanced(tc)}")