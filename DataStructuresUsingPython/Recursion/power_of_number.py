def power_of_number(x, n):
    assert 0 <= n == int(n), "The exponent must be positive integer!!"
    if n == 0:
        return 1
    else:
        return x * power_of_number(x, n - 1)


base = input("Enter a number: ")
power = input("Enter the power: ")

print(power_of_number(float(base), float(power)))
