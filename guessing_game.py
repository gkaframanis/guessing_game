import random
from art import logo

print(f"{logo}\n")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "hard":
    number_of_guesses = 5
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
else:
    number_of_guesses = 10
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")


while number_of_guesses > 0: 
    guess = int(input("Make a guess: "))
    
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print(f"You got it! The answer was {guess}.")
        break

    number_of_guesses -= 1
    if number_of_guesses >= 1:
        print("Guess again.")
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")

    if number_of_guesses == 0:
        print("You've run out of guesses, you lose.")



