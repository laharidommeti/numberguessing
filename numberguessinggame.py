print("A secret number awaits... Can you crack it ???")
print("I've selected the number between 1 and 100")

while True:
    try:
        guess = int(input("Go ahead,have a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
number_guessing_game()
