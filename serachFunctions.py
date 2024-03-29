import time
import matplotlib.pyplot as plt


# Search functions
def linear_search(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def measure_search_time(search_function, list_size, target):
    lst = list(range(list_size))
    start_time = time.perf_counter()
    search_function(lst, target)
    end_time = time.perf_counter()
    return round(end_time - start_time, 6)


def draw_results(results, title):
    list_size = [val[0] for val in results]
    execution_time = [val[1] for val in results]
    plt.scatter(list_size, execution_time, label=title)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('List Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Search Performance')
    plt.legend()
    plt.grid(True, which="both", ls="--")

if __name__ == "__main__":
    nums = [2**x for x in range(1, 21)]
    results_linear = []
    results_binary = []
    for num in nums:
        time_linear = measure_search_time(linear_search, num, -1)  
        time_binary = measure_search_time(binary_search, num, -1)
        results_linear.append((num, time_linear))
        results_binary.append((num, time_binary))
    
    plt.figure(figsize=(10, 6))
    draw_results(results_linear, 'Linear Search')
    draw_results(results_binary, 'Binary Search')
    plt.show()
