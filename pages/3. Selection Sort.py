import streamlit as st
import matplotlib.pyplot as plt

# Streamlit App
st.title("Study of the Sorting Method: Selection Sort")

st.subheader("1. Description")
st.write("Selection sort is a simple comparison-based sorting algorithm that divides the list into two parts: the sorted and the unsorted portions. During each iteration, the algorithm selects the smallest (or largest, depending on the sorting order) element from the unsorted portion and swaps it with the first element of the unsorted portion. This process continues until the entire list is sorted.")

st.subheader("2. Pseudo-code")
st.code("""
Input: Array T of size n
Output: Array T sorted in ascending order

For i from 1 to n-1 do:
    posmin = i
    For j from i+1 to n do:
        If T[j] < T[posmin] then:
            posmin = j
        EndIf
    EndFor
    If posmin != i then:
        temp = T[posmin]
        T[posmin] = T[i]
        T[i] = temp
    EndIf
EndFor
""", language="plaintext")

st.subheader("3. Complexity")
st.write("""
The time complexity of the Selection Sort algorithm in different cases is:
 - Best case: O(n^2)
 - Worst case: O(n^2)
 - Average case: O(n^2)
""")

st.write("""
**Source**  
This information is based on the *Improved Selection Sort Algorithm* article from the *International Journal of Computer Applications (Vol. 110, No. 5, January 2015)*.
""")

st.subheader("4. Python Implementation")
st.code("""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
""", language="python")

st.subheader("5. Experimental Results")

# Input data
n_values = [1000, 2000, 4000, 8000, 16000, 32000]
execution_times = [453.0177 ,1355.1507 ,5006.6361 ,19484.6797 ,77335.5479 ,305920.6686]  

# Display results in a table
st.write("Execution Time (ms):")
results_table = {"Array Size (n)": n_values, "Time (ms)": execution_times}
st.dataframe(results_table)

# Graph Representation
fig, ax = plt.subplots()
ax.plot(n_values, execution_times, label="Selection Sort", marker="o", color="green")
ax.set_xlabel("Array Size (n)")
ax.set_ylabel("Execution Time (ms)")
ax.set_title("Performance of Selection Sort")
ax.legend()
st.pyplot(fig)
