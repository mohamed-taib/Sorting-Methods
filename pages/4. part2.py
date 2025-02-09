import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data for execution times (in milliseconds)
n_values = [1000, 2000, 4000, 8000, 16000, 32000]

# Insertion Sort execution times
insertion_times = [567.7580833, 207.291613, 797.3861933, 3068.419576, 118626.4246, 487326.458]

# Selection Sort execution times
selection_times = [453.0177116, 1355.1507, 5006.636143, 19484.6797, 77335.54792, 305920.6686]

# Heap Sort execution times
heap_sort_times = [117.1557903, 232.3684692, 567.2478676, 928.4939766, 1987.812519, 4102.551699]

# Theoretical complexities (constant values based on the algorithms)
insertion_theoretical = [n**2 for n in n_values]  # O(n²)
selection_theoretical = [n**2 for n in n_values]  # O(n²)
heap_sort_theoretical = [n * np.log2(n) for n in n_values]  # O(n log n)

# Streamlit App
st.title("Comparison of Sorting Algorithms: Theoretical Complexity")

st.subheader("1. Experimental Execution Times")

# Convert the results to a DataFrame for display
results_table = pd.DataFrame({
    "Array Size (n)": n_values,
    "Insertion Sort Time (ms)": insertion_times,
    "Selection Sort Time (ms)": selection_times,
    "Heap Sort Time (ms)": heap_sort_times
})
st.dataframe(results_table)

st.subheader("2. Theoretical Time Complexities of Sorting Algorithms")

# Plotting theoretical complexities
n = np.linspace(1, 32000, 1000)  # Input size range for plotting

# Theoretical time complexity curves
selection_sort_theoretical = n**2
insertion_sort_best = n  # Best case (O(n))
insertion_sort_worst = n**2  # Worst case (O(n^2))
heap_sort_theoretical_curve = n * np.log2(n)

plt.figure(figsize=(10, 6))
plt.plot(n, selection_sort_theoretical, label='Selection Sort (O(n^2))', linestyle='--', color='blue')
plt.plot(n, insertion_sort_best, label='Insertion Sort Best Case (O(n))', linestyle='-', color='green')
plt.plot(n, insertion_sort_worst, label='Insertion Sort Worst Case (O(n^2))', linestyle='--', color='green')
plt.plot(n, heap_sort_theoretical_curve, label='Heap Sort (O(n log n))', linestyle='-', color='red')

plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')
plt.title('Comparison of Sorting Algorithms Time Complexity')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

st.write("""
### Selection Sort:
- Its curve is very steep because it always takes \(O(n^2)\) time, no matter the input.
- This makes it slow for large datasets.

### Insertion Sort:
- When the data is already sorted, it’s much faster (\(O(n)\)), shown by the straight, gentle line.
- But for reversed or random data, it becomes as slow as Selection Sort (\(O(n^2)\)), with a steep curve.

### Heap Sort:
- Its curve grows slowly compared to the others because it takes \(O(n \log n)\) time.
- This makes Heap Sort consistently faster for larger inputs.

### Summary:
- **For small or sorted data**: Insertion Sort is a good choice.
- **For large datasets**: Heap Sort is more efficient.
- **Selection Sort**: It’s generally not used because it’s always slow.
""")

st.subheader("3. Experimental Time Complexities of Sorting Algorithms")

# Plotting experimental times
plt.figure(figsize=(10, 6))
plt.plot(n_values, insertion_times, label='Insertion Sort', linestyle='-', marker='o', color='green')
plt.plot(n_values, selection_times, label='Selection Sort', linestyle='-', marker='o', color='blue')
plt.plot(n_values, heap_sort_times, label='Heap Sort', linestyle='-', marker='o', color='red')

plt.xlabel('Array Size (n)')
plt.ylabel('Time (ms)')
plt.title('Comparison of Sorting Algorithm Times (Experimental)')
plt.legend(title='Sort Types')
plt.grid(True)
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

# Observations section

st.write("""
### Insertion Sort and Selection Sort:
- Both exhibit quadratic time complexity (\(O(n^2)\)). This is evident from the steep upward curve of their lines as the input size (\(n\)) increases.
- Insertion Sort appears to have slightly better performance than Selection Sort for smaller input sizes, but the difference becomes negligible as \(n\) grows larger.

### Heap Sort:
- Heap Sort has a more favorable time complexity of \(O(n \log n)\). This is reflected in the relatively gentle upward curve, indicating that its execution time increases more slowly with input size.
- Heap Sort consistently outperforms both Insertion Sort and Selection Sort, especially for larger datasets.

### General Trend:
- The graph demonstrates that Heap Sort is significantly more efficient than Insertion Sort and Selection Sort for larger datasets.
- The quadratic growth rate of Insertion Sort and Selection Sort becomes a major bottleneck for large inputs, making them impractical for real-world applications.

### Conclusion:
Heap Sort is the clear winner in terms of time complexity for this experiment. Insertion Sort and Selection Sort, while simpler to implement, are not suitable for large-scale sorting tasks due to their quadratic time complexity.
""")
