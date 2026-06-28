import random 
n = random.randint(1,100)
guess = 0
while guess != n:
    guess =int(input("Enter a number btw 1-100"))
    if guess > n:
        print("High!")
    elif guess < n:
        print("Low!")
    else:
        print("You guessed it!")
        
