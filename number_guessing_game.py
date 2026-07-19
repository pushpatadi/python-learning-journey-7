print("🎮 Welcome to Number Guessing Game!")

secret_number = 7

user = int(input("Guess a number between 1 and 10: "))

while user != secret_number:

    if user < secret_number:
        print("Too small ! Try again")
    else :
        print("Too high ! Try again")

    user = int(input("Enter new Guess: "))

