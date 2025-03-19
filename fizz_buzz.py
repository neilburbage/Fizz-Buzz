print("Welcome to the game.\n")
print("Choose a number divisible by 3, 5, or 15 to get the password.\n")

def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print("Fizz Buzz")
        return True
    elif (num % 3 == 0):
        print("Fizz Buzz")
        return True    
    elif (num % 5 == 0):
        print("Fizz Buzz")
        return True
    else:
        print("Try again") 
        return False 
           
while True:
    try:
        n = int(input("input a number between 1 and 100\n"))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue

    if n < 1 or n > 100:
        print("Try again")
        continue

    if fizz_buzz(n):
        break
        

    