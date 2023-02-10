import time
import matplotlib.pyplot as plt

def fib_original(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_original(n-1) + fib_original(n-2)

def fib_memo(n, store={}):
    if n == 0 or n == 1:
        return n
    if n in store:
        return store[n]
    else:
        store[n] = fib_memo(n-1, store) + fib_memo(n-2, store)
        return store[n]

x_values = list(range(36))
y_values_original = []
y_values_memo = []

for i in range(36):
    start_time = time.time()
    result = fib_original(i)
    end_time = time.time()
    y_values_original.append(end_time - start_time)

    start_time = time.time()
    result = fib_memo(i)
    end_time = time.time()
    y_values_memo.append(end_time - start_time)

plt.plot(x_values, y_values_original, label="Code-given")
plt.plot(x_values, y_values_memo, label="My-code")
plt.xlabel("n value")
plt.ylabel("Execution time (seconds)")
plt.legend()
plt.show()
