first = str(input("Whats your first name? "))
last = str(input("Whats your last name? "))

def greet (first, last):

    if last and first:
         greeting = "Hello there," + first + " of " + last + "! Cool name bro! :)"  
    
    elif last:
         greeting = "Hi, " + last

    elif first:
         greeting = "Hello, " + first + "."

    else:
         greeting = "No name, huh? GET THIS MAN OUT OF HERE"

    return greeting


print(greet(first, last))