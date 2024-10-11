def fibonacci(num):
    fibseries = []
    a = 0
    b = 1

    for i in range(num):
        fibseries.append(a)
        a,b = b, a+b

    return fibseries

terms = int(input("Enter a number: "))

if terms <= 0:
    print("Please enter a +ve number")
else:
    series = fibonacci(terms)
    print("Series = ", series)