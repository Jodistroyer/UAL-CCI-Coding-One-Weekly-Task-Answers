# Write a program that outputs “even” if a number is even and “odd” if a number is odd.

try:
    # Input a number as a string and convert it to a float
    num_str = float(input("Please input a number: "))
    num = float(num_str)

    # Check if the number is even or odd
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter a valid number.")
