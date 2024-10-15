num = int(input("Enter a number: "))

digits = str(num)
numdigits = len(digits)

armstrongsum = 0
for digit in digits:
    armstrongsum += int(digit) ** numdigits

if armstrongsum == num:
    print(num, " is an armstrong number")
else:
    print(num, " is not an armstrong number")