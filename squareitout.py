odd = []
even = []

def generatesquares(start, end):
    squares = [i ** 2 for i in range(start, end + 1)]
    return squares


def seperateoddeven(squares):
    oddsquares = [square for square in squares if square % 2 != 0]
    evensquares = [square for square in squares if square % 2 == 0]
    return oddsquares, evensquares

startrange = int(input("Enter start of range: "))
endrange = int(input("Enter end of range: "))

squares = generatesquares(startrange, endrange)

oddsquares, evensquares = seperateoddeven(squares)

print(f"\nSquares of numbers from {startrange} to {endrange}: \n{squares}")
print(f"\nEven squares:\n{evensquares}")
print(f"\nOdd squares:\n{oddsquares}")