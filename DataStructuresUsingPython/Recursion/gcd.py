def gcd(a,b):
    assert 0 <= a == int(a) and 0 <= b == int(b), "The numbers must be positive integers!!"
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print(gcd(int(num1), int(num2)))