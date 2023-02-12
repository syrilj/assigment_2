import sys
import json
import matplotlib.pyplot as plt
import time

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Read data from the JSON file
with open("ex2.5.json", "r") as f:
    arr_raw = json.load(f)
arr = []
for element in arr_raw:
    if isinstance(element, list):
        # If the element is a list, convert its elements to numbers
        arr.extend([int(x) for x in element])
    else:
        # If the element is not a list, convert it to a number
        arr.append(int(element))

low = 0
high = len(arr) - 1

start_time = time.time()
func1(arr, low, high)
end_time = time.time()

# Plot the timing results
time_points = [start_time, end_time]
execution_time = [0, end_time - start_time]
plt.plot(time_points, execution_time)
plt.xlabel("Time (seconds)")
plt.ylabel("Execution Time")
plt.title("Quick Sort Timing Results")
plt.show()

print(end_time-start_time)
#import random 
# Partially sort the data by randomly swapping elements
#for i in range(len(arr_raw) // 2):
 #   j = random.randint(i, len(arr_raw) - 1)
  #  arr_raw[i], arr_raw[j] = arr_raw[j], arr_raw[i]

# Save the partially sorted arr_raw to a new JSON file
#with open("ex2.5.json", "w") as file:
#    json.dump(arr_raw, file)