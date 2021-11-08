def product_of_array(arr):
    assert 0 < len(arr), "The array must have at least one numerical value!!"
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * product_of_array(arr[1:])


values = [2, 4, 6, 8, 9]
print(product_of_array(values))
