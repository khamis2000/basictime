import time
import matplotlib.pyplot as plt

# Inefficient recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Efficient memoized Fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Measure execution time
def measure_fibonacci_time(fibonacci_function, n):
    start_time = time.perf_counter()
    fibonacci_function(n)
    end_time = time.perf_counter()
    return round(end_time - start_time, 6)

# Plot results
def draw_results(results, title):
    list_size = [val[0] for val in results]
    times = [val[1] for val in results]
    plt.figure(figsize=(10, 6))
    plt.plot(list_size, times, marker='o', linestyle='-', color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Nth Fibonacci Number')
    plt.ylabel('Execution Time (s)')
    plt.title(title)
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    input_sizes = [2**i for i in range(0, 11)]  # From 1 to 2^10
    results_recursive = []
    results_memoized = []
    
    for n in input_sizes:
        # For larger values, skip the recursive method to avoid long execution times
        if n <= 30:
            time_recursive = measure_fibonacci_time(fibonacci_recursive, n)
            results_recursive.append((n, time_recursive))
        
        time_memoized = measure_fibonacci_time(fibonacci_memoized, n)
        results_memoized.append((n, time_memoized))
    
    # Plot results for recursive method
    print("Recursive Fibonacci Results:")
    draw_results(results_recursive, "Recursive Fibonacci Performance")
    
    # Plot results for memoized method
    print("Memoized Fibonacci Results:")
    draw_results(results_memoized, "Memoized Fibonacci Performance")
