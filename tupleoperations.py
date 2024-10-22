def calculateproduct(numbers):
    product = 1
    for number in numbers:
        product += number
    return product

mytuple = (2, 3, 4, 5)
result = calculateproduct(mytuple)

print("The product of all numbers in the tuple ", mytuple, " is", result, ".")