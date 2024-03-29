import time
import matplotlib.pyplot as plt

# Inefficient naive count
def naive_count_words(text):
    words = text.split()
    count = {}
    for word in words:
        count[word] = sum(1 for w in words if w == word)
    return count

# Efficient hash table count
def hash_table_count_words(text):
    words = text.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

# Measure execution time
def measure_word_count_time(count_function, number_of_words):
    text = " ".join(["word"] * number_of_words)  # Generating a text with a repeated word
    start_time = time.perf_counter()
    count_function(text)
    end_time = time.perf_counter()
    return round(end_time - start_time, 6)

# Plot results
def draw_results(results):
    list_size = [val[0] for val in results]
    times = [val[1] for val in results]
    plt.figure(figsize=(10, 6))
    plt.plot(list_size, times, marker='o', linestyle='-', color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Number of Words')
    plt.ylabel('Execution Time (s)')
    plt.title('Word Count Performance')
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    input_sizes = [10**i for i in range(1, 5)]  # 10, 100, 1,000, 10,000 words
    results_naive = []
    results_hash = []
    
    for size in input_sizes:
        time_naive = measure_word_count_time(naive_count_words, size)
        results_naive.append((size, time_naive))
        
        time_hash = measure_word_count_time(hash_table_count_words, size)
        results_hash.append((size, time_hash))
    
    # Plot results for naive count
    print("Naive Count Results:")
    draw_results(results_naive)
    
    # Plot results for hash table count
    print("Hash Table Count Results:")
    draw_results(results_hash)
