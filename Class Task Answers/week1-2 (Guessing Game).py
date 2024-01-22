import random

## rerun code in loop (https://stackoverflow.com/questions/11459102/how-do-i-re-run-code-in-python#:~:text=You%20need%20to%20bury%20the%20code%20block%20in%20another%20code%20block.&text=What%20you%20are%20doing%20is,Hope%20this%20helps.)

count = 0 ## start the count value (https://stackoverflow.com/questions/26665663/how-can-i-count-how-many-tries-ive-taken)

while True:

    a = int(input("Please guess a number ")) ## input field
    b = random.randint(0,10)              ## guess a random number from 1 to 10 (https://www.tutorialspoint.com/generating-random-number-list-in-python)
                            

    if a > b:
        print("You guessed too large!")
        print ('\n','Try again!','\n')
        count+=1                          ## increment count for every wrong answer
        print ("You had %d tries" %count)   ## let user know how many tries he had
        print(a)

    elif a < b:
        print("You guessed too small!")
        print ('\n','Try again!','\n')
        count+=1                         
        print ("You had %d tries" %count)
        print(a) 

    else:
        print ("You guessed correctly!")
        print ("You had %d tries" %count)
        break