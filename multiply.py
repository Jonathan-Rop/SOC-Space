def multiply_numbers(*args):
    
    result = 1
    for num in args:
        result *= num
    return result

result = multiply_numbers(2, 3, 4)
print("Result:", result)  # Output: Result: 24
