def decimal_to_binary(n):
    assert 0 <= n == int(n), "The number must be a positive integer!!"
    if n == 1:
        return 1
    else:
        return decimal_to_binary(int(n / 2)) * 10 + n % 2


num = input("Enter a number: ")
print(decimal_to_binary(int(num)))