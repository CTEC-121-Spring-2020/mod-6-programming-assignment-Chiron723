# Module 7
#   Programming Assignment 10
#     Prob-3.py

# <Stephen Guild>

def main():
    sum = 0.0
    #count = 0
    #x = float(input("Enter a number (negative to quit) >> "))
    #while x >= 0:
        #sum += x
        #count += 1
        #x = float(input("Enter a number (negative to quit) >> "))
    #print("\nThe average of the numbers is", sum / count)

    # do not change the while loop definition below
    while True:
        number=float(input("enter a positive number: "))
        if number>=0:
            sum+=number
        else:
            break
    print("the sum of the numbers entered is",sum)

main()    