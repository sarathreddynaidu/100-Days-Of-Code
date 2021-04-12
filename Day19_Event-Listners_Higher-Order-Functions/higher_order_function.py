def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(a, b, func):
    return func(a, b)


result1 = calculate(45, 10, add)
result2 = calculate(45, 10, subtract)
result3 = calculate(45, 10, multiply)
result4 = calculate(45, 10, divide)

print(result1)
print(result2)
print(result3)
print(result4)
