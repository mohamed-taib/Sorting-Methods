import streamlit as st
import matplotlib.pyplot as plt

# Streamlit App
st.title("Study of the Sorting Method: Insertion Sort")

st.subheader("1. Description")
st.write("Insertion sort divides the list into two parts: sorted and unsorted. It iterates through the unsorted part, comparing each element with the sorted part to place it in the correct position. This process is repeated until the entire list is sorted.")

st.subheader("2. Pseudo-code")
st.code("""
# Insertion Sort
Input: Array T of size n
Output: Array T sorted in ascending order

For i from 1 to n-1 do:
    temp = T[i]
    j = i
    While j > 0 and T[j-1] > temp do:
        T[j] = T[j-1]
        j = j - 1
    EndWhile
    T[j] = temp
EndFor
""", language="plaintext")

st.subheader("3. Complexity")
st.write("""
        - Best case: O(n) (when the array is already sorted).
        - Worst case: O(n^2) (when the array is sorted in reverse order).
        - Average case: O(n^2).
         """)

st.subheader("4. Python Implementation")
st.code("""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
""", language="python")

st.subheader("5. Experimental Results")

# Input data
n_values = [1000, 2000, 4000, 8000, 16000, 32000]
execution_times = [567.7581 ,207.2916 ,797.3862 ,3068.4196 ,118626.4246 ,487326.458]  

# Display results in a table
st.write("Execution Time (ms):")
results_table = {"Array Size (n)": n_values, "Time (ms)": execution_times}
st.dataframe(results_table)

# Graph Representation
fig, ax = plt.subplots()
ax.plot(n_values, execution_times, label="Insertion Sort", marker="o", color="orange")
ax.set_xlabel("Array Size (n)")
ax.set_ylabel("Execution Time (ms)")
ax.set_title("Performance of Insertion Sort")
ax.legend()
st.pyplot(fig)
