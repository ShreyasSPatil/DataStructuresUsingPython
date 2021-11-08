def factorial(n):
    assert 0 <= n == int(n), "The number must be positive and and a integer!!"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


num = input("Enter a number: ")
print(factorial(int(num)))
