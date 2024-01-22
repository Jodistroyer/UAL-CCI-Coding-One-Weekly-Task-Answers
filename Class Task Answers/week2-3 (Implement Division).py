#Implement division as a series of subtraction. The program should only deal with integers and report the remainder if there is one. eg. 10/2 => 10-2-2-2-2-2=0, 10 minus 2 five times so the division result is 5 with a remainder of 0

a = 10
b = 2

for i in range(1, a):
    a = a - b

    if a - b < 0:
        print(i)
        print("Remainder:", a)
        break