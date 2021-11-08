def fibonacci(n):
    assert 0 <= n == int(n), "The number must be positive and integer!!!"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = input("Enter the index: ")
print(fibonacci(int(num)))