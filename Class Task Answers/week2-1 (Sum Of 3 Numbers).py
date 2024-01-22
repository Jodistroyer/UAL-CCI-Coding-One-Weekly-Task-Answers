# Given 3 positive integers, find the sum of all numbers between the first two that are a multiple of the third. eg. Given "1, 10, 2", the expected output is "20".

# a = input("first: ")
# b = input("second: ")
# c = input("third: ")

startingRange = 1
endingRange = 10
multiple = 2

# Create a variable to store the sum
sum_of_i = 0

for i in range(startingRange, endingRange):         # Find all numbers within range
    if i % multiple == 0:                           # Single out multiples using Modulo Operator
        sum_of_i += i                               # Add all multiples to the sum (https://www.codecademy.com/learn/introduction-to-python-dvp/modules/python-syntax-dvp/cheatsheet)

# Print the final sum
print(sum_of_i)

#you must define before u can use it