import random
chances = 0
number = random.randint(1, 9)
print("Number Guessing Game")
print("Guess a number from 1-9. Try to get the correct number. You have 5 chances!")

while chances < 5: 
    guess = int(input("Enter your guess: "))
    if guess==number:
        print("Congratulations! You won!")
        break

    elif guess>number:
        print("Guess a number lower than ", guess)
    
    else:
        print("Guess a number higher than ", guess)

    chances = chances + 1

if not chances < 5: 
    print("Oops! You lose! The number was ", number , ".")

