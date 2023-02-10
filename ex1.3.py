def func(n, store={}):
    if n == 0 or n == 1:
        return n
    if n in store:
        return store[n]
    else:
        store[n] = func(n-1, store) + func(n-2, store)
        return store[n]


print(func(35))