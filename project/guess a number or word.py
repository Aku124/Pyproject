import random

print("\nMenu:")
print("1. Guess a Number")
print("2. Guess a Word")
print("3. Quit")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    print("Welcome to the Guess a Number game!")

    lower = int(input("Enter Lower bound: "))
    upper = int(input("Enter Upper bound: "))

    secret_number = random.randint(lower, upper)
    max_attempts = round(math.log(upper - lower + 1, 2))
    print("\nYou have only", max_attempts, "chances to guess the integer!")

    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        guess = int(input("Guess a number: "))

        if guess == secret_number:
            print("Congratulations! You guessed it in", attempts, "tries!")
            break
        elif guess < secret_number:
            print("Too small! Try again.")
        else:
            print("Too large! Try again.")

    if attempts >= max_attempts:
        print("\nThe number was", secret_number)
        print("Better luck next time!")

elif choice == 2:
    name = input("What is your name? ")
    print("Good Luck ! ", name)

    words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

    word = random.choice(words)
    print("Guess the characters")

    guesses = ''
    turns = 12

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        if failed == 0:
            print("\nYou Win")
            print("The word is: ", word)
            break
        guess = input("\nguess a character: ")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
