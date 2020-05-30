# Module 7
#   Programming Assignment 10
#     Prob-1.py

# <Stephen Guild>

def main():
    sum = 0.0
    count = 0
    x = float(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        sum += x
        count += 1
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the numbers is", sum / count)

main()    