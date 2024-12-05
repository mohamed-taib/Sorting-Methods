import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

# Heap Sort Implementation
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Measure execution times
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())  # Use a copy to avoid modifying the original array
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

# Streamlit App
st.title("Study of Sorting Methods: Heap Sort")

st.subheader("1. Description")
st.write("Heap sort is an efficient comparison-based sorting algorithm that works by converting the list into a binary heap structure (max-heap or min-heap) and repeatedly extracting the root element, which is the largest or smallest, to sort the list.")

st.subheader("2. Pseudo-algorithm")
st.code("""
# Heap Sort
Input: Array T of size n
Output: Array T sorted in ascending order

# Build Max-Heap
For i from n/2 down to 1 do:
    Call heapify(T, i, n)
EndFor

# Extract elements from heap
For i from n down to 2 do:
    Swap T[1] with T[i]
    Decrease heap size by 1
    Call heapify(T, 1, i-1)
EndFor

# Heapify subroutine
heapify(T, i, heapSize):
    largest = i
    left = 2 * i
    right = 2 * i + 1
    If left <= heapSize and T[left] > T[largest] then:
        largest = left
    EndIf
    If right <= heapSize and T[right] > T[largest] then:
        largest = right
    EndIf
    If largest != i then:
        Swap T[i] with T[largest]
        Call heapify(T, largest, heapSize)
    EndIf
""", language="plaintext")

st.subheader("3. Complexity")
st.write("""
        - Best case: O(nlog⁡n).
        - Worst case: O(nlog⁡n).
        - Average case: O(nlog⁡n).
         """)

st.subheader("4. Python Implementation")
st.code("""
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
""", language="python")

st.subheader("5. Experimental Results")

# Input data for worst case scenario
n_values = [1000, 2000, 4000, 8000, 16000, 32000]
execution_times = [117.1558 , 232.3685 ,567.2479 ,928.494 ,1987.8125 ,4102.5517]
# Display the table with results
st.write("Execution Times (ms):")
results_table = {"Array Size (n)": n_values, "Time (ms)": execution_times}
st.dataframe(results_table)

# Graph Representation
fig, ax = plt.subplots()
ax.plot(n_values, execution_times, label="Heap Sort", marker="o")
ax.set_xlabel("Array Size (n)")
ax.set_ylabel("Execution Time (ms)")
ax.set_title("Heap Sort Performance")
ax.legend()
st.pyplot(fig)
