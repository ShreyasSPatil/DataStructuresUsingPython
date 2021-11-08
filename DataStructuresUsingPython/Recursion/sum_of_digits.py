def sum_of_digits(n):
    assert 0 <= n == int(n), "The number must be a positive integer!!"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n / 10))


num = input("Enter a number: ")
print(sum_of_digits(int(num)))
