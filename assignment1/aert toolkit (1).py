class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x) 

    def pop(self):
        if not self.is_empty():
            return self.items.pop() 
        return None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None 

    def is_empty(self):
        return len(self.items) == 0 

    def size(self):
        return len(self.items) 

# --- Global counters for Fibonacci calls [cite: 79] ---
naive_calls = 0
memo_calls = 0
memo_dict = {}

def factorial(n):
    if n < 0: return None 
    if n == 0 or n == 1: return 1 
    return n * factorial(n - 1)

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1: return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n):
    global memo_calls
    memo_calls += 1
    if n in memo_dict: return memo_dict[n]
    if n <= 1: return n
    memo_dict[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo_dict[n]

def hanoi(n, source, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}") 
        return
    hanoi(n - 1, source, dest, aux)
    print(f"Move disk {n} from {source} to {dest}")
    hanoi(n - 1, aux, source, dest)

def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1 
    mid = (low + high) // 2
    stack.push(mid)  
    
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)

def run_tests():
    print("--- Part B: Factorial ---")
    for n in [0, 1, 5, 10]:   
        print(f"Factorial({n}) = {factorial(n)}")

    print("\n--- Part B: Fibonacci (Naive vs Memo) ---")
    global naive_calls, memo_calls, memo_dict
    for n in [5, 10, 20, 30]: 
        naive_calls = 0
        memo_calls = 0
        memo_dict = {}
        ans_memo = fib_memo(n)
        ans_naive = fib_naive(n)
        print(f"n={n}: Result={ans_memo} | Naive Calls={naive_calls} | Memo Calls={memo_calls}")

    print("\n--- Part C: Tower of Hanoi (N=3) ---")
    hanoi(3, 'A', 'B', 'C') 

    print("\n--- Part D: Binary Search ---")
    test_arr = [1, 3, 5, 7, 9, 11, 13]
    keys = [7, 1, 13, 2] 
    search_stack = StackADT()
    for k in keys:
        res = binary_search(test_arr, k, 0, len(test_arr)-1, search_stack)
        print(f"Search {k}: Index {res}")
    
    print("\nMid-indices visited (from StackADT):", end=" ")
    while not search_stack.is_empty():
        print(search_stack.pop(), end=" ")

if __name__ == "__main__":
    run_tests()