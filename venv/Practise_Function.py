import math

def square(x):
    result = []
    for y in x:
        result.append(math.pow(y,2.0))
    return result

print(square([1,2,3]))

def square(vals, result=None):
    if result is None:
        result = []
    result.extend(v*v for v in vals)
    return result
print(square([1,4,3]))

def doubleNumbers(numbers):
    results = []  # we'll collect our results in here
    for x in numbers:
        results.append(x + x)
    return results
print(doubleNumbers([1, 2, 3, 4, 5]))
